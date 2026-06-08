import threading, time, sys


output_lock = threading.Lock()

def background_worker(worker_name, sleep_duration):
    sys.stdout.write(f"[{worker_name}] Starting background task...\n")

    time.sleep(sleep_duration)

    with output_lock:
        sys.stdout.write(f"[{worker_name}] Task finished smoothly after {sleep_duration}s!\n")


t1 = threading.Thread(target=background_worker, args=("Worker-Alpha", 2.0))
t2 = threading.Thread(target=background_worker, args=("Worker-Beta", 3.0))

t1.start()
t2.start()
sys.stdout.write("[Main Execution] Both threads launched. I can keep running code here immediately!\n")

t1.join()
t2.join()

sys.stdout.write("[Main Execution] All background threads finished. Exiting.\n")
