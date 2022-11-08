

queueItems = ['a', 'e', 'i', 'o']

def printItems(items):
    queue = []
    #create queue
    for i in items:
        queue.append(i)
    #print queue
    for i in range(len(queue)):
        print(queue[0])
        queue[0]

printItems(queueItems)