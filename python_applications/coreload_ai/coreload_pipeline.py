import sys, time, socket, subprocess, sqlite3
import threading


def main():
    process = subprocess.Popen(
        ["python3", "model_mock.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    conn = sqlite3.connect("ai_telemetry.db")
    cursor = conn.cursor()
    model_logs = cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS model_logs (
        input_data TEXT,
        classification TEXT,
        memory_count_ref INTEGER)"""
    )
    conn.commit()
    conn.close()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 8888))
    s.listen(1)
    tele_device, internal_val = s.accept()
    t = threading.Thread(target=handle_network_stream, args=(conn, process))
    t.start()

def handle_network_stream(conn, process):

