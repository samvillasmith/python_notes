# When to use multithreading:
'''
1. I/O-bound tasks: When your program spends a lot of time waiting 
for I/O operations (like reading/writing files, network requests, etc.), 
multithreading can help by allowing other threads to run while one is waiting for I/O.
2. CPU-bound tasks: If you have tasks that require a lot of CPU processing, 
you might consider using multiprocessing instead of multithreading, 
as Python's Global Interpreter Lock (GIL) can be a bottleneck for CPU-bound tasks.
3. Concurrent tasks: When you have multiple tasks that can run concurrently
   and do not depend on each other, multithreading can help improve the responsiveness 
   of your application by allowing these tasks to run in parallel.
'''

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")

def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()


t = time.time()
finished_time = time.time() - t
print(finished_time)