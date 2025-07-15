from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number: {number}"

def square_number(number):
    time.sleep(1)
    return f"Number: {number * number}"

if __name__ == "__main__":
    # ThreadPoolExecutor code
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    print("Using ThreadPoolExecutor:")
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_number, numbers)

    for result in results:
        print(result)

    # ProcessPoolExecutor code
    numbers2 = [1,2,3,4,5,6,7,8,9]

    print("\nUsing ProcessPoolExecutor:")
    with ProcessPoolExecutor(max_workers=3) as executor:
        square_results = executor.map(square_number, numbers2)

    for square_result in square_results:
        print(square_result)