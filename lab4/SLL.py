import random

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self, data = 0):
        self.head = node(data)

    def add(self, data):
        newNode = node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode

    def getList(self):
        list = []
        temp = self.head
        while temp != None:
            list.append(temp.data)
            temp = temp.next 
        return list

    def getLen(self):
        len = 0
        temp = self.head
        while temp != None:
            len += 1
            temp = temp.next 
        return len

    def search(self, target):
        temp = self.head
        while temp is not None:
            if not temp.next:
                return f'{target} not in list'
            if temp.data == target:
                return temp.data
            else:
                temp = temp.next

    def delete(self, target):
        temp = self.head
        while temp is not None:
            if not temp.next:
                return f'{target} not in list'
            if temp.next.data == target:
                temp.next = temp.next.next
                return f'{target} removed'
            else:
                temp = temp.next

    def deleteNth(self, n):
        temp = self.head
        for i in range(n):
            temp = temp.next
            if not temp.next.next:
                if i == 1:
                    deletedData = temp.next.data
                    temp.next = None
                    return f'{deletedData} removed'
                else:
                    return 'number is too large'
        deletedData = temp.next.data
        temp.next = temp.next.next
            
        


    def sort(self):
        # len = self.getLen()
        swapped = 1
        while swapped:
            swapped = 0
            temp = self.head
            while temp is not None:
                if not temp.next:
                    break
                currentData = temp.data
                nextData = temp.next.data
                if currentData > nextData:
                    temp.data = nextData
                    temp.next.data = currentData
                    swapped = 1
                temp = temp.next
        return 'List sorted'

    def reverse(self):
        list  = self.getList()
        newHead = node(list.pop())
        tempHead = newHead
        for i in range(len(list)):
            tempHead.next = node(list.pop())
            tempHead = tempHead.next
        self.head = newHead
        return 'List Reversed'





list = SLL()
for i in range(random.randint(10, 25)):
    list.add(random.randint(0, 9))




print('\nGenerated list:')
print(list.getList())

print('\nSearching for 2 random numbers')
print(list.search(random.randint(0, 9)))
print(list.search(random.randint(0, 9)))


print('\nDeleting 3 random values')
print(list.delete(random.randint(0, 9)))
print(list.delete(random.randint(0, 9)))
print(list.delete(random.randint(0, 9)))
print(list.getList())

print('\nDeleting 3 random numbers from n-th')
length = list.getLen()
print(list.deleteNth(random.randint(0, length)))
print(list.deleteNth(random.randint(0, length)))
print(list.deleteNth(26))
print(list.getList())

print('\nSorting list')
print(list.sort())
print(list.getList())

print('\nReverse list')
print(list.reverse())
print(list.getList())


