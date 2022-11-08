import time
testArr = range(10000000000)
target = 29410093


def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1
    midpoint = (start + end) // 2
    while arr[midpoint] != target:
        midpoint = (start + end) // 2
        if start > end:
            return f'{target} is not in array'
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] > target:
            end = midpoint - 1
        else:
            start = midpoint + 1


startTime = time.time()
ans = binarySearch(testArr, target)
endTime = time.time()
print(f'found {ans} in {(endTime - startTime) * 1000}')
