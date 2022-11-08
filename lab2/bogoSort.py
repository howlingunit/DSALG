import random

testArr = []
for i in range(10):
    testArr.append(random.randint(0, 9))



print(f'Test arr:     {testArr}')

def bubbleSort(arr):
    for i in range(len(arr)):
        arr[i] = arr[random.randint(0, len(arr) - 1)]            
    return arr


print(f'\nSorted array: {bubbleSort(testArr)}')
