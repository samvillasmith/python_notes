'''
In the real world, CPU-bound tasks like calculating factorials can benefit from 
multi-processing. This example demonstrates how to accomplish this using Python's
multiprocessing module.
'''

import multiprocessing
import math
import sys
import time

# increase the max number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# compute the factorial of a given number
def compute_factorial(number):
    print(f"Computing the factorial of {number}")
    result = math.factorial(number)
    print(f"The factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [5000, 6000, 7000]

    start_time = time.time()

    # create a worker process pool
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")