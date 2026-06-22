import time
import random


def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1
    probes = 0

    while low <= high and key >= arr[low] and key <= arr[high]:

        probes += 1

        if low == high:
            if arr[low] == key:
                return low, probes
            return -1, probes

        if arr[high] == arr[low]:
            break

        pos = low + ((key - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if pos < low or pos > high:
            break

        if arr[pos] == key:
            return pos, probes

        elif arr[pos] < key:
            low = pos + 1

        else:
            high = pos - 1

    return -1, probes


print("=" * 60)
print("INTERPOLATION SEARCH ON USER-DEFINED DATASETS")
print("=" * 60)

print("\nChoose Dataset Type")
print("1. Uniformly Distributed Dataset")
print("2. Non-Uniformly Distributed Dataset")

dataset_choice = int(input("Enter your choice (1/2): "))

print("\nChoose Data Input Method")
print("1. Enter Elements Manually")
print("2. Generate Random Data")

input_choice = int(input("Enter your choice (1/2): "))

arr = []

# Manual Input
if input_choice == 1:

    n = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(n):
        arr.append(int(input()))

# Random Data Generation
elif input_choice == 2:

    n = int(input("Enter number of elements: "))

    if dataset_choice == 1:
        # Uniform Dataset
        start = random.randint(1, 20)
        step = random.randint(1, 5)

        for i in range(n):
            arr.append(start + i * step)

    else:
        # Non-Uniform Dataset
        value = random.randint(1, 10)

        for i in range(n):
            value += random.randint(1, 50)
            arr.append(value)

    print("\nGenerated Dataset:")
    print(arr)

# Check if sorted
is_sorted = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

if not is_sorted:

    print("\nDataset is not sorted.")
    choice = input("Do you want to sort it? (yes/no): ")

    if choice.lower() == "yes":
        arr.sort()
        print("\nSorted Dataset:")
        print(arr)
    else:
        print("Interpolation Search requires sorted data.")
        exit()

print("\nDataset Used:")
print(arr)

key = int(input("\nEnter the search key: "))

start_time = time.perf_counter()

index, probes = interpolation_search(arr, key)

end_time = time.perf_counter()

execution_time = (end_time - start_time) * 1000

print("\nSEARCH RESULT")
print("-" * 40)

if index != -1:
    print("Key Found")
    print("Index Position :", index)
else:
    print("Key Not Found")

print("Number of Probes/Comparisons :", probes)
print("Execution Time :", round(execution_time, 6), "ms")

print("\nPERFORMANCE ANALYSIS")
print("-" * 40)

if dataset_choice == 1:
    print("Dataset Type : Uniform Distribution")
    print("Expected Performance : Better")
    print("Average Complexity : O(log log n)")
else:
    print("Dataset Type : Non-Uniform Distribution")
    print("Expected Performance : Slower")
    print("Average Complexity may degrade toward O(n)")

print("\nCONCLUSION")
print("-" * 40)
print("Interpolation Search estimates the probable")
print("position of the search key.")
print("It performs efficiently on uniformly")
print("distributed datasets.")
print("For non-uniform datasets, the estimated")
print("position may be inaccurate, leading to")
print("more probes and reduced performance.")
