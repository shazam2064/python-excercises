import threading

import time


def myfuction():
    print("Start a thread")
    time.sleep(3)
    print("End a thread")


threads = []

for i in range(5):
    th = threading.Thread(target=myfuction())

for th in threads:
    th.join()
