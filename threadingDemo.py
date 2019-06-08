import threading
import time
from queue import Queue


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    time.sleep(2)
    q.put(l)


def multithreading():
    q = Queue()
    threads = []
    data = [[1, 2, 3], [2, 4, 6], [6, 7, 8], [5, 5, 5]]
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    result = []
    for x in range(4):
        result.append(q.get())
    print(result)


if __name__ == '__main__':
    time_start = time.perf_counter()
    multithreading()
    time_end = time.perf_counter()
    print('program use %ss'% (time_end - time_start))
