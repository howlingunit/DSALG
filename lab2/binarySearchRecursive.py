import time
testArr = range(10000000000)

target = 29410093


def binarySearch(arr, target, start=0, end=0, midpoint = 0):
    if not end:
        end = len(arr) - 1

    if arr[midpoint] == target:
        return midpoint

    midpoint = (start + end) // 2

    if start > end:
        return f'{target} is not in array'
    elif arr[midpoint] > target:
        end = midpoint - 1
        midpoint = binarySearch(arr, target, start, end, midpoint)
        return midpoint
    else:
        start = midpoint + 1
        midpoint = binarySearch(arr, target, start, end, midpoint)
        return midpoint


startTime = time.time()

ans = binarySearch(testArr, target)

endTime = time.time()

print(f'found {ans} in {(endTime - startTime) * 1000}')
