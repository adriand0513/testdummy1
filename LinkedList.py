# create a Node class 
class Node:
    # instantialize it with a value and the 'next' to point to the next node
    def __init__(self, data):
        self.data = data 
        self.next = None

# create a LinkedList class
class LinkedList:
    
    # instantialize the first node 'self.head' to none because it has no "current" value in the beginning
    def __init__(self):
        self.head = None

    # create a display method to display the linked list on the terminal 
    def display(self):
        # set the first node to current
        current = self.head
        # while there is an existing node, iterate until there are no values
        while current:
            print(current.data, end=" -> ")
            current = current.next
        # print "None" for when there is no data or there is no more nodes that holds a value
        print("None")

    # create a add last method 
    def append(self, data):
        # create a node object that has data, a value
        new_node = Node(data)
        # if there are no values in the first node, place this new node first
        if not self.head:
            self.head = new_node
            return
        # otherwise, iterate throughout the list until there is a node with no value next to it.
        current = self.head
        while current.next:
            current = current.next
        # set the new node to very last node
        current.next = new_node
    # create a insert in the beginning method
    def insert_at_beginning(self, data):
        # create a new Node object
        new_node = Node(data)
        # link the first existing node to the new node
        new_node.next = self.head
        # set the new node to the first node
        self.head = new_node
