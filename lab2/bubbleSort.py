import random

testArr = []
for i in range(1000):
    testArr.append(random.randint(0, 99))



print(f'Test arr: {testArr}')

def bubbleSort(arr):
    for i in range(len(arr)):
        for x in range(len(arr) - 1):
            elm1 = arr[x]
            elm2 = arr[x+1]
            if elm1 > elm2:
                arr[x] = elm2
                arr[x+1] = elm1
    return arr


print(f'\nSorted array: {bubbleSort(testArr)}')
