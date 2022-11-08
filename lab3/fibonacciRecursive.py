import time

def fibonacciSequence(target = 0, n = 0, m = 1, arr = [], i = 0):
    arr.append(n)
    i+=1
    if n == target:
        return n
    if target < n:
        return arr
    else:
        nth = n+m
        m = n
        n = nth
        return fibonacciSequence(target, n, m, arr, i)

startTime = time.time()
ans = fibonacciSequence(6765)
endTime = time.time()
print(f'found {ans} in {(endTime - startTime) * 1000}')
# 0 1 1 2 3 5
