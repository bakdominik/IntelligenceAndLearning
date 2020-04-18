import random

class Node():
    
    # Create tree object
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    # Display all numbers in tree
    def show(self):
        if self.left:
            self.left.show()
        print( self.data),
        if self.right:
            self.right.show()

    # Add new value to the tree
    def insert(self,data):
        if self.data:
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            elif data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
        else:
            self.data = data

    # Search for value in tree
    def search(self,number):
        if number == self.data:
            return self
        elif number > self.data and self.right != None:
            return self.right.search(number)
        elif self.left != None:
            return self.left.search(number)
        return None



tree = Node(10)
for i in range(10):
    tree.insert(random.randint(0,20))
tree.show()
print(tree.search(5))
