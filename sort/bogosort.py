import random
import time

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bogosort(arr):
    attempts = 0
    start_time = time.time()
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
    print(f"Sorted after {attempts} shuffles!")
    end_time = time.time()
    runtime = end_time - start_time
    return runtime

times = []

for i in range(0, 20):
    arr = [random.randint(0, 7) for j in range(10)]
    runtime = bogosort(arr)
    times.append(runtime)
    
print(times)