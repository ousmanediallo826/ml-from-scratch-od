import os, sys, socket, sqlite3, time



FIFO_PATH = "/tmp/mainframe_fifo"

if not os.path.exists(FIFO_PATH):
    os.mkfifo(FIFO_PATH)

# ==============================================================================
# 1. DATABASE LAYER: SCHEMA INITIALIZATION
# ==============================================================================

def initiate_database():
    conn = sqlite3.connect("ledger.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mainframe_ledger (
    account_id TEXT,
    value REAL, 
    timestamp TEXT)""")

    conn.commit()
    conn.close()


# ==============================================================================
# 3. FORKS, PIPES, SOCKET, AND SHELL UTILITIES PIPELINE
# ==============================================================================

def socket_and_forking_init():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 9999))

    server_socket.listen(1)

    client_conn, client_addr = server_socket.accept()
    r, w = os.pipe()
    pid =os.fork()


    if pid == 0:
        os.close(r)

        fifo_write = os.open(FIFO_PATH, os.O_WRONLY)
        while True:
            data = client_conn.recv(1024)
            if not data:
                break
            os.write(fifo_write, data)
        client_conn.close()
        os.close(fifo_write)
        sys.stdout.write(f"[Child] Disconnected. Stream ended.\n")
        sys.exit(0)
    else:
        sys.stdout.write(f"[Parent-{os.getpid()}] Database consumer online.\n")
        fifo_read = os.open(FIFO_PATH, os.O_RDONLY)

        db_conn = sqlite3.connect("ledger.db")
        db_cursor = db_conn.cursor()

        pipe_stream = os.fdopen(fifo_read, "r")

        for line in pipe_stream:
            clean_line = line.strip()

            if not clean_line:
                continue
            sys.stdout.write(f"[Parent] Captured Live Line: {clean_line}\n")

            try:
                parts = clean_line.split(" | ")

                acct = parts[1].split(":")[1]
                val = float(parts[2].split(":")[1])
                currents_tms = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


                db_cursor.execute(
                    "INSERT INTO mainframe_ledger VALUES (?, ?, ?)",
                    (acct, val, currents_tms)
                )

                db_conn.commit()
                sys.stdout.write(f"  -> Account {acct} transaction saved to SQL ledger.\n")
            except Exception as parse_error:
                db_conn.rollback()
                sys.stderr.write(f"[Parent Error] Failed processing or saving log line: {parse_error}\n")

        pipe_stream.close()
        os.wait()
        db_conn.close()
        sys.stdout.write("[Hub] Master transaction cycle completed successfully.\n")

















if __name__ == '__main__':
    initiate_database()
    socket_and_forking_init()


