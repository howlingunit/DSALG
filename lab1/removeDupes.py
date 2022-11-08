testArr = [1, 1, 2, 4, 7, 7, 8]

def removeDupes(arr):
  stack = []
  x = 0
  y = 0
  while arr:
    if i == 0:
      x = arr.pop()
      stack.append(x)
      continue

    x = arr.pop()
    y = arr.pop()
    if y == x:
      continue
    else:
      stack.append(y)
    


  return stack

print(removeDupes(testArr))
