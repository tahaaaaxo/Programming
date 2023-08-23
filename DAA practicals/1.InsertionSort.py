import random
import time


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


# Generate an array of random numbers
arr_size = 1000
arr = [random.randint(0, 100) for _ in range(arr_size)]

# Perform the experiment for arrays of different sizes
for size in [2000, 3000, 4000, 5000]:
    # Generate an array of random numbers
    arr = [random.randint(0, 100) for _ in range(size)]

    # Measure the time it takes to sort the array using Insertion Sort
    start_time = time.time()
    insertion_sort(arr)
    end_time = time.time()

    # Print the results
    print(f"Size: {size}, Time: {end_time - start_time} seconds")
