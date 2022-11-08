import time

def findNumInSeq(target):
    n = 0
    m = 1
    while n < target:
        nth = n + m
        m = n
        n = nth

    if n == target:
        return n 
    else:
        return ''



startTime = time.time()
ans = findNumInSeq(5000)
endTime = time.time()
print(f'found {ans} in {(endTime - startTime) * 1000}')