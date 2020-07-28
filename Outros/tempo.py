import time, sys

def tempo():
    for i in range(1, 31):
        sys.stdout.write(f"\r{i}")
        sys.stdout.flush()
        time.sleep(1)
    print ("\nQue pena, seu tempo acabou")


tempo()