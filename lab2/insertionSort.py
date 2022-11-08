import random

testArr = []
for i in range(1000):
    testArr.append(random.randint(0, 99))


def insertionSort(arr):
    for i in range(len(arr)):
        current = arr[i]
        currentIndex = i
        while currentIndex > 0 and current < arr[currentIndex-1]:
            arr[currentIndex] = arr[currentIndex - 1]


            currentIndex -= 1
        arr[currentIndex] = current

    return arr
            

print(f'\nSorted array: {insertionSort(testArr)}')