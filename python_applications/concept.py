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









#====================2. Python and the Shell=========================
import subprocess
import os
import time
result = subprocess.run("pwd")
print(f"Terminal exit code: {result.returncode}")

capture_result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print("--- Captured Shell Output ---")
print(capture_result.stdout)


try:
    subprocess.run(["cat", "missing_textbook_file.txt"], check=True, capture_output=True, text=True)
except subprocess.CalledProcessError as error:
    print("--- Failed to capture shell output ---")
    print(error.output)


custom_env = os.environ.copy()

custom_env["LIBRARY_ACCESS_TOKEN"] = "SECRET_CAMPUS_PASS_123"
subprocess.run(["python3", "practice.py"], env=custom_env)



process = subprocess.Popen(["ping", "-c", "5", "8.8.8.8"], stdout=subprocess.PIPE, text=True)
print("Python: I started the network ping in the background! Moving on...")

for line in process.stdout:
    print(f"Live Stream Data From Shell -> {line.strip()}")

process.wait()
print("Background shell job complete.")










#=====================3. Forks and Forking==============================
print(f"Initial Process Baseline PID: {os.getpid()}")

pid = os.fork()

if pid == 0:
    print(f"Greetings from the CHILD! My unique system PID is: {os.getpid()}")
    sys.exit(0)

else:
    print(f"Greetings from the PARENT! I just birthed Child Process PID: {pid}")




pid = os.fork()
if pid == 0:
    print("Child: Starting short data calculation task...")
    time.sleep(2)
    print("Child: Task complete. Exiting clean.")
    sys.exit(0)

else:
    print("Parent: I am pausing to wait for my child process to wrap up...")
    finished_pid, status =os.wait()
    print(f"Parent: Child {finished_pid} has been safely reaped with status code {status}.")



shared_inventory = ["Book A", "Book B", "Book C"]
pid = os.fork()
if pid == 0:
    shared_inventory.append("Chilled modify book D")
    print(f"Child Inventory State: {shared_inventory}")
    sys.exit(0)

else:
    os.wait()
    print(f"Parent Inventory State: {shared_inventory}")

