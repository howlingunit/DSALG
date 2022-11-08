testArr = [5, 3, 4, 1, 2]
target = 1

def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


print(linearSearch(testArr, target))