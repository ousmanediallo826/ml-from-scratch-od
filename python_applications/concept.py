#=====================1. sys-Module=============================
import sys

print(f"Script Name: {sys.argv[0]}")
print(f"Arguments Passed: {sys.argv[1:]}")
print(f"Total count: {len(sys.argv)}")


sys.stdout.write("Processing library card enrollment... ")
sys.stderr.write("ERROR: Database connection timeout!\n")

for path in sys.path:
    print(path)







sys.path.append("/Users/ousmanediallo/Desktop/custom_library_tools")

empty_list  = []

field_list = [i for i in range(1000)]
print(f"Empty list: Memory overhead: {sys.getsizeof(empty_list)} bytes")
print(f"Field list: Memory overhead: {sys.getsizeof(field_list)} bytes")


library_books = ["The Great Gatsby", "Moby Dick"]

print(sys.getrefcount(library_books))

check_out_queue = library_books
print(sys.getrefcount(library_books))




#
# user_access_level = "Admin"
#
# if user_access_level != "Admin":
#     sys.stderr.write("ERROR: User access level not allowed!\n")
#     sys.exit(1)
# print("Welcome to the the secure database model.")
# sys.exit(0)

#
#
#
#
#
#
#
#
# #====================2. Python and the Shell=========================
# import subprocess
# import os
# import time
# result = subprocess.run("pwd")
# print(f"Terminal exit code: {result.returncode}")
#
# capture_result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
# print("--- Captured Shell Output ---")
# print(capture_result.stdout)
#
#
# try:
#     subprocess.run(["cat", "missing_textbook_file.txt"], check=True, capture_output=True, text=True)
# except subprocess.CalledProcessError as error:
#     print("--- Failed to capture shell output ---")
#     print(error.output)
#
#
# custom_env = os.environ.copy()
#
# custom_env["LIBRARY_ACCESS_TOKEN"] = "SECRET_CAMPUS_PASS_123"
# subprocess.run(["python3", "practice.py"], env=custom_env)
#
#
#
# process = subprocess.Popen(["ping", "-c", "5", "8.8.8.8"], stdout=subprocess.PIPE, text=True)
# print("Python: I started the network ping in the background! Moving on...")
#
# for line in process.stdout:
#     print(f"Live Stream Data From Shell -> {line.strip()}")
#
# process.wait()
# print("Background shell job complete.")
#
#
#
#
#
#
#
#
#
#
# #=====================3. Forks and Forking==============================
# print(f"Initial Process Baseline PID: {os.getpid()}")
#
# pid = os.fork()
#
# if pid == 0:
#     print(f"Greetings from the CHILD! My unique system PID is: {os.getpid()}")
#     sys.exit(0)
#
# else:
#     print(f"Greetings from the PARENT! I just birthed Child Process PID: {pid}")
#
#
#
#
# pid = os.fork()
# if pid == 0:
#     print("Child: Starting short data calculation task...")
#     time.sleep(2)
#     print("Child: Task complete. Exiting clean.")
#     sys.exit(0)
#
# else:
#     print("Parent: I am pausing to wait for my child process to wrap up...")
#     finished_pid, status =os.wait()
#     print(f"Parent: Child {finished_pid} has been safely reaped with status code {status}.")
#
#
#
# shared_inventory = ["Book A", "Book B", "Book C"]
# pid = os.fork()
# if pid == 0:
#     shared_inventory.append("Chilled modify book D")
#     print(f"Child Inventory State: {shared_inventory}")
#     sys.exit(0)
#
# else:
#     os.wait()
#     print(f"Parent Inventory State: {shared_inventory}")
#
#
#
#
# #========================4. Threads and Threading==========================
# import threading
# def check_printer_status(printer_id: str):
#     print(f"[Thread-{printer_id}]: Checking toner and printer level")
#     time.sleep(2)
#     print(f"[Thread-{printer_id}] Printer check complete.")
#
# thread1 = threading.Thread(target=check_printer_status, args=("PRN-01",))
# thread2 = threading.Thread(target=check_printer_status, args=("PRN-02",))
#
# thread1.start()
# thread2.start()
#
# thread01 = thread1.join()
# thread02 = thread2.join()
#
#
# print("Main Script: Both printer threads finished. Updating library dashboard.")
#
#
# total_student_count = 0
#
# counter_lock = threading.Lock()
#
# def student_gate_scanner():
#     global total_student_count
#     for _ in range(100000):
#         with counter_lock:
#             total_student_count += 1
# gate1 = threading.Thread(target=student_gate_scanner)
# gate2 = threading.Thread(target=student_gate_scanner)
#
# gate1.start()
# gate2.start()
#
# gate1.join()
# gate2.join()
#
# print(f"Final safe student count: {total_student_count}")


#=====================5. Pipes in Python========================
import os
r, w = os.pipe()

print(f"Read Descriptor handle: {r}")
print(f"Write Descriptor handle: {w}")
os.write(w, b"Library Turnstile Alert: Guest check in")
message_bytes = os.read(r, 1024)
print(f"Received from Pipe: {message_bytes.decode()}")
os.close(r)
os.close(w)


import sys
import time

pid = os.fork()
r, w = os.pipe()
if pid == 0:
    os.close(r)
    print("[CHILD] Analyzing gate telemetry logs...")
    time.sleep(2)

    os.write(w, b"METRIC:ROOM101:OCCUPANCY:5")
    os.close(w)
    sys.exit(0)

else:
    os.close(w)
    print("[Parent] Pausing until the child transmits analytics through the pipe...")

    data  = os.read(r, 1024)
    print(f"[Parent] Captured data capsule out of the pipe: {data.decode()}")
    os.close(r)
    os.wait()

#
# import os
# import time
#
# PIPE_PATH = "/tmp/library_fifo"
#
# # Create the named pipe file if it doesn't exist on disk yet
# if not os.path.exists(PIPE_PATH):
#     os.mkfifo(PIPE_PATH)
#
# print("Transmitter: Opening pipe line. Waiting for a consumer to connect...")
#
# # Opening a FIFO for writing blocks the script until someone opens it to read
# fifo_write = os.open(PIPE_PATH, os.O_WRONLY)
#
# print("Transmitter: Consumer connected! Streaming data loops...")
# for i in range(5):
#     message = f"LOG_ROW_{i}: Student turned in book reserve.\n"
#     os.write(fifo_write, message.encode())
#     time.sleep(1)
#
# os.close(fifo_write)
# print("Transmitter: Streaming finished.")



#======================6. Python Network Scanner=======================
# import sys, socket
#
# TARGET_IP = "127.0.0.1"
# TARGET_PORT = 80
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# s.settimeout(1.0)
#
# result = s.connect_ex((TARGET_IP, TARGET_PORT))
#
#
# if result == 0:
#     sys.stdout.write(f"Port {TARGET_PORT}: OPEN (Service Active)\n")
#
# else:
#     sys.stdout.write(f"Port {TARGET_PORT}: CLOSED (No response, error code: {result})\n")
#
#
#
# def scan_port_range(target_ip: str, start_port: int, end_port: int):
#     sys.stdout.write(f"INIT: Commencing network sweep across {target_ip}...\n")
#
#     for port in range(start_port, end_port + 1):
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.settimeout(0.1)
#
#         result = s.connect_ex((target_ip, port))
#         if result == 61:
#             sys.stdout.write(f"Port {port}: OPEN (Service Active)\n")
#         s.close()
#
#         sys.stdout.write("Sweep complete.\n")
#
#

# if __name__ == "__main__":
#     if len(sys.argv) < 4:
#         sys.stderr.write(f"Usage Guide: python3 {sys.argv[0]} <IP> <Start-Port> <End-Port>\n")
#         sys.exit(1)
#
#     scan_port_range(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))


import socket
import threading
import sys
import time

open_ports_discovered = []
print_lock = threading.Lock()

def check_target_port(target_host: str, port_number: int):
    """Worker function handed to an independent concurrent thread."""

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)

        result = s.connect_ex((target_host, port_number))

        if result == 0:
            open_ports_discovered.append(port_number)
            with print_lock:
                sys.stdout.write(f"[ALERT] Found Open Doorway -> Port {port_number} is ACTIVE.\n")
        s.close()
    except Exception:
        pass




def run_threaded_scanner(target_host: str, ports_to_scan: list):
    start_time = time.time()
    thread_pool = []

    sys.stdout.write(f"Launching concurrent multi-threaded engine against: {target_host}\n")

    for port in ports_to_scan:
        t = threading.Thread(target=check_target_port, args=(target_host, port, ports_to_scan))
        thread_pool.append(t)

        t.start()


    for t in thread_pool:
        t.join()
    duration = time.time() - start_time
    sys.stdout.write(f"\n--- SCAN SUMMARY FOR {target_host} ---\n")
    sys.stdout.write(f"Execution completed in {duration:.2f} seconds.\n")
    sys.stdout.write(f"Active Ports Detected: {sorted(open_ports_discovered)}\n")


if __name__ == "__main__":
    # Scan a broad structural sequence of standard server doorways (SSH, HTTP, HTTPS, etc.)
    COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 443, 8080]
    TARGET = "127.0.0.1"  # Target localhost

    run_threaded_scanner(TARGET, COMMON_PORTS)

