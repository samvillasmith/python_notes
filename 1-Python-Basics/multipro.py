import multiprocessing

import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"square {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube {i*i*i}")

if __name__ == "__main__":
    # Create 2 processes 
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()

    # start the process
    p1.start()
    p2.start()

    # Wait for the processes to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t 
    print(finished_time)