import sys, time

while True:
    input_line = sys.stdin.readline().strip()
    if not input_line:
        break
    sys.stdout.write(f"PROCESSED_CLASSIFICATION:{input_line}\n")
    sys.stdout.flush()



