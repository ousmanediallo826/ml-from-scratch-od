import sys, os

read_handle, write_handle = os.pipe()
pid = os.fork()


if pid == 0:

    os.close(read_handle)

    import time

    time.sleep(1.5)

    message = "ALERT: Data packet successfully validated."

    os.write(write_handle, message.encode())
    os.close(write_handle)
    sys.exit(0)
else:
    os.close(write_handle)
    print("[Parent] Standing by. Listening for the child process to push data into the pipe...")

    pipe_reader = os.fdopen(read_handle, "r")

    for message in pipe_reader:
        print(f"[Parent Log Received] -> {message}")

    pipe_reader.close()
    os.wait()
