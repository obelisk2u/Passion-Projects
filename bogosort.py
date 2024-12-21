import random

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bogosort(arr):
    attempts = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
    print(f"Sorted after {attempts} shuffles!")
    return arr

arr = [3, 1, 4, 1, 5, 745, 34, 6, 8, 0]
print("Original array:", arr)
sorted_arr = bogosort(arr)
print("Sorted array:", sorted_arr)
