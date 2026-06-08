import sys, os, time


pid = os.fork()

if pid == 0:
    print(f"[CHILD]-{os.getpid()} is running...")
    sys.stdout.write(f"alert [CHILD-{os.getpid()}] cannot modify system configuration files ")
    sys.exit(0)
else:
    os.wait()
    print(f"[CHILD]-{os.getpid()} has completed its tasks and that system integrity remains intact.")