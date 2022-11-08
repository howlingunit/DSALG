
def hashes(x):
    if x > 0:
        hashes(x//2)
        hashes(x//2)
    print(x)

hashes(5)