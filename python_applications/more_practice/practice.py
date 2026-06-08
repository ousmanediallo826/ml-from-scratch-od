import os, sys

shared_book_count = 10

print(f"Before the fork, Process ID: {os.getpid()}")


pid =  os.fork()

if pid == 0:
    shared_book_count = 999
    print(f"[CHILD]-{os.getpid()} I modified the count to: {shared_book_count}")

    sys.exit(0)


else:
    import time
    time.sleep(0.5)
    print(f"[Parent-{os.getpid()}] The child is done.")
    print(f"[Parent] My book count is still: {shared_book_count}")

    os.wait()







#=========================🔌 Concept 2: Network Sockets (socket)===========================

