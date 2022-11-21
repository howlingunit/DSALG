class Node:
    def __init__(self, data):
        self.leftNode = None
        self.rightNode = None
        self.data = data

    def add(self, data):
        nodeData = self.data
        if data < nodeData:
            if self.leftNode == None:
                self.leftNode = Node(data)
            else:
                self.leftNode.add(data)
        else:
            if self.rightNode == None:
                self.rightNode = Node(data)
            else:
                self.rightNode.add(data)

class Binary_tree:
    def __init__(self, data):
        self.root = Node(data)

    def add(self, data):
        root = self.root
        root.add(data)

    def inOrderTreversal(self, node = 'root'):
        if node == 'root':
            node = self.root

        if node is not None:
            self.inOrderTreversal(node.leftNode)
            print(node.data)
            self.inOrderTreversal(node.rightNode)

    def preOrderTreversal(self, node = 'root'):
        if node == 'root':
            node = self.root

        if node is not None:
            print(node.data)
            self.preOrderTreversal(node.leftNode)
            self.preOrderTreversal(node.rightNode)

    def postOrderTreversal(self, node = 'root'):
        if node == 'root':
            node = self.root

        if node is not None:
            self.postOrderTreversal(node.leftNode)
            self.postOrderTreversal(node.rightNode)
            print(node.data)
    
    def removeNode(self, target):
        node = self.root
        prevNode = None

        while node.data is not target:
            prevNode = node
            if node.leftNode is None and node.rightNode is None:
                return None
            elif node.data < target:
                node = node.rightNode
            else:
                node = node.leftNode

        # find minimum
        targetNode = node
        replacmentNode = None

        if node.leftNode is None and node.rightNode is None:
            replacmentNode = None # leaf
        
        elif node.leftNode is None:
            replacmentNode = node.rightNode
        
        elif node.rightNode is None:
            replacmentNode = Node.leftNode

        else:
            tempRight = node.rightNode
            tempLeft = node.leftNode

            node = node.leftNode
            while node.rightNode:
                replaceParentNode = node
                node = node.rightNode

            replaceParentNode.rightNode = None
            if node.leftNode:
                replaceParentNode = replacmentNode.leftNode

            replacmentNode = node
            replacmentNode.leftNode = tempLeft
            replacmentNode.rightNode = tempRight

        if prevNode is not None:
            if prevNode.data > targetNode.data:
                prevNode.leftNode = replacmentNode

            else:
                prevNode.rightNode = replacmentNode



# test cases 

tree = Binary_tree(2)
tree.add(8)
tree.add(3)
tree.add(4)
tree.add(1)
tree.add(11)
tree.add(9)

# print('\nin order traversal:')
# tree.inOrderTreversal()
# print('\npre order traversal:')
# tree.preOrderTreversal()
# print('\npost order traversal:')
# tree.postOrderTreversal()


print('\nRemoving node 8')
tree.removeNode(8)
tree.inOrderTreversal()

print('\nRemoving node 1')
tree.removeNode(1)
tree.inOrderTreversal()


print('\nRemoving node 3')
tree.removeNode(3)
tree.inOrderTreversal()

print('\nRemoving node 9')
tree.removeNode(9)
tree.inOrderTreversal()
