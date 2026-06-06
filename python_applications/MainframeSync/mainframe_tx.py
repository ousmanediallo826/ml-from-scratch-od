import sys, socket, time
from mainframesync_hub import *


if __name__ == '__main__':
    initiate_database()
    socket_and_forking_init()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(("127.0.0.1", 999))
        sys.stdout.write("[SIMULATOR] Successfully connected to Ingestion Hub!\n")

    except socket.error as error:
        sys.stderr.write(error)
        sys.stderr.write("Make sure your main hub script is running and listening first!\n")
        sys.exit(1)

    for i in range(5):
        payload = f"TX_ID:10054 | ACCT:88392 | VAL:450.75 | STATUS:CLEARED | BATCH:{i}\n"
        sys.stdout.write(f"[SIMULATOR] Transmitting data capsule {i}...\n")
        s.send(payload.encode())
        time.sleep(1)

    s.close()
    sys.stdout.write("[SIMULATOR] Stream finalized. Disconnected from hub safely.\n")
