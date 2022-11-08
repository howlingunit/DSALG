

# def circle():
#     circle = []
#     head = 0
#     tail = 0
#     sizeOfCircle = 10

#     for i in range(sizeOfCircle):
#         circle.append
#         head+=1 % sizeOfCircle
#         (tail-=1 + sizeOfCircle) % sizeOfCircle
#     print('s')

class Circle:
    def __init__(self, _size = 10):
        self.size = _size
        self.array = [0] * _size
        self.head = 0
        self.tail = 0

    def addToCircle(self, item):
        self.array[self.head] = item
        self.head = (self.head + 1) % self.size

    def getFromCircle(self):
        output = self.array.pop(self.tail)
        self.array.insert(self.tail, 0)
        self.tail = (self.tail - 1) % self.size
        return output

    def getArr(self):
        return self.array

c1 = Circle(10)
print(c1.getArr())
for i in range(10):
    c1.addToCircle(i)
print(c1.getArr())

for i in range(10):
    print(c1.getFromCircle())

print(c1.getArr())