class node():
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def next(self):
        if (self.next_node is not None):
            return self.next_node
        else:
            return "end"

    def create(self, x):
        if(self.next_node is not None):
            self.next_node.create(x)
        else:
            self.next_node = node(x)

root_node = node(3)
root_node.create(4)
root_node.create(2)

print ( root_node.value )
print( root_node.next().value )
print( root_node.next().next().value )
print( root_node.next().next().next() )
