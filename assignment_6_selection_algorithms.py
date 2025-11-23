import random
import time
import math


# Deterministic Selection Algorithm: Median of Medians (worst-case O(n))
def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Step 1: Divide the array into groups of 5
    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    # Step 2: Sort each group and find the median
    medians = [sorted(group)[len(group) // 2] for group in groups]

    # Step 3: Recursively find the median of medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Step 4: Partition the array around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_list = [x for x in arr if x == pivot]

    # Step 5: Determine which side contains the kth smallest element
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + len(pivot_list):
        return pivot
    else:
        return median_of_medians(high, k - len(low) - len(pivot_list))


# Randomized Selection Algorithm: Randomized Quickselect (average-case O(n))
def randomized_quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_list = [x for x in arr if x == pivot]

    if k < len(low):
        return randomized_quickselect(low, k)
    elif k < len(low) + len(pivot_list):
        return pivot
    else:
        return randomized_quickselect(high, k - len(low) - len(pivot_list))


# Performance Analysis and Empirical Testing
def time_comparison():
    sizes = [10, 100, 1000, 10000]
    for size in sizes:
        arr = random.sample(range(1, 100000), size)

        # Time the deterministic algorithm
        start = time.time()
        median_of_medians(arr, size // 2)
        end = time.time()
        print(f"Median of Medians (size={size}): {end - start:.5f} seconds")

        # Time the randomized algorithm
        start = time.time()
        randomized_quickselect(arr, size // 2)
        end = time.time()
        print(f"Randomized Quickselect (size={size}): {end - start:.5f} seconds")


if __name__ == "__main__":
    # Example usage
    arr = [7, 2, 3, 6, 4, 5, 1]
    k = 3  # k-th smallest element (0-indexed)

    print(f"Deterministic Selection (Median of Medians): {median_of_medians(arr, k)}")
    print(f"Randomized Selection (Quickselect): {randomized_quickselect(arr, k)}")

    # Perform time comparison
    time_comparison()
