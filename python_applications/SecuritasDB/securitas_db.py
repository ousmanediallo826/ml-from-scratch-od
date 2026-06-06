import os
import sys
import time
import sqlite3
import socket
import threading
import subprocess
from functools import wraps


# ==============================================================================
# 1. DATABASE LAYER: SCHEMA INITIALIZATION
# ==============================================================================


DB_FILE = "security_audit.db"
def init_database():
    """Builds a persistent relational database layout to record audit anomalies."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS port_alerts (
        alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
        host_ip TEXT NOT NULL,
        port_number INTEGER NOT NULL,
        diagnostic_log TEXT,
        timestamp TEXT NOT NULL)
        """
    )
    conn.commit()
    conn.close()


# ==============================================================================
# 2. THREADING LAYER: CONCURRENT NETWORK DOORWAY PROBING (I/O-BOUND)
# ==============================================================================


pipe_lock = threading.Lock()

def check_target_port(host: str, port: int, write_fd: int):
    """
        Runs a non-blocking TCP socket connection check.
        Drops the GIL automatically during network handshake latency windows.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((host, port))
    if result == 0:
        alert_payload = f"{host}:{port}\n"

        with pipe_lock:
            os.write(write_fd, alert_payload.encode())
            sys.stdout.write(f"[Thread-Scanner] EXPOSED PORT TRACKED -> {host}:{port}\n")

    s.close()

# ==============================================================================
# 3. FORKS, PIPES, AND SHELL UTILITIES PIPELINE
# ==============================================================================


def execute_system_audit(target_ip: str, port_list: list):
    """
        Splits application execution across CPU walls via os.fork() and links
        processes together using an anonymous kernel communications pipe.
    """

    sys.stdout.write(f"\n[Master-{os.getpid()} Starting full systems audit...\n")

    r, w = os.pipe()
    pid = os.fork()

    if pid == 0:
        os.close(r)
        scanner_threads = []
        for port in port_list:
            t = threading.Thread(target=check_target_port, args=(target_ip, port, w))
            scanner_threads.append(t)
            t.start()

        for t in scanner_threads:
            t.join()

        os.close(w)
        sys.stdout.write(f"[Child-{os.getpid()}] Network sweep complete. Terminating process cleanly.\n")
        sys.exit(0)

    else:
        os.close(w)
        sys.stdout.write(f"[Parent-{os.getpid()}] Network consumer online. Awaiting stream updates...\n")

        db_conn = sqlite3.connect(DB_FILE)
        db_cursor = db_conn.cursor()
        
        
        pipe_reader = os.fdopen(r, 'r')
        for line in pipe_reader:
            host_ip, port_num = line.strip().split(":")
            sys.stdout.write(f"\n[Parent] Processing alert capsule for exposed port {port_num}...\n")

            shell_logs = "Diagnostic lookup skipped"

            try:
                diagnostic_run = subprocess.run(
                    ["ping", "-c", "2", host_ip],
                    check=True,
                    capture_output=True,
                    text=True
                )
                shell_logs = diagnostic_run.stdout.strip()
            except subprocess.CalledProcessError as e:
                shell_logs =f"Traceroute failure: {e.stderr}"


            try:
                record = (host_ip, int(port_num), shell_logs, time.strftime("%Y-%m-%d %H:%M:%S"))

                db_cursor.execute("INSERT INTO port_alerts (host_ip, port_num, shell_logs, timestamp) VALUES (?, ?, ?, ?)", record)
                db_conn.commit()

                sys.stdout.write(f"[Parent] Alert for Port {port_num} committed to database storage safely.\n")
            except sqlite3.Error as sql_error:
                db_conn.rollback()
                sys.stderr.write(f"[DATABASE-ERROR] Transaction failed! Rolled back data modifications: {sql_error}\n")


        pipe_reader.close()
        os.wait()
        db_conn.close()
        sys.stdout.write(f"\n[Master-{os.getpid()}] System architecture sweep finalized successfully.\n")



# ==============================================================================
# MAIN ENGINE ENTRY POINT
# ==============================================================================

if "__main__" == __name__:
    if len(sys.argv) < 2 or sys.argv[1].lower() != "--audit":
        sys.stderr.write("CRITICAL CONFIG FAULT: Missing required tracking flags.\n")
        sys.stderr.write(f"Usage Guide: python3 {sys.argv[0]} --audit\n")
        sys.exit(1)

    init_database()

    TARGET_HOST = "127.0.0.1"

    PORTS_ARRAY = [22, 80, 443]
    execute_system_audit(TARGET_HOST, PORTS_ARRAY)
    sys.exit(0)
