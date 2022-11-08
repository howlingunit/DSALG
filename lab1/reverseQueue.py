inputQueue = [5, 4, 3, 2, 1]

def reverseQueue(queue):
    stack = []
    output = ''
    for i in range(len(queue)):
        x = queue.pop(0)
        stack.append(x)
    while stack:
        output += str(stack.pop())

    print(output)
reverseQueue(inputQueue)
