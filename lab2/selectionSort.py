import random

testArr = []
for i in range(1000):
    testArr.append(random.randint(0, 99))



print(f'Test arr: {testArr}')

def selectionSort(arr):
    sortedArr = []


    for i in range(len(arr)):
        smallest = arr[0]
        for x in range(len(arr)):
            if smallest > arr[x]:
                smallest = arr[x]
        
        sortedArr.append(arr.pop(arr.index(smallest)))

    return sortedArr

print(f'\nSorted array: {selectionSort(testArr)}')