#!python

from linkedlist import LinkedList


# implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack"""
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack"""
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty"""
        if self.is_empty():
            return None
        else:
            return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty"""
        if self.is_empty():
            raise ValueError('List is empty')
        else:
            head = self.list.head.data
            self.list.delete(self.list.head.data)
            return head


# implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        # Initialize a new dynamic array to store the items
        self.list = list()
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        if len(self.list) == 0:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this stack"""
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack"""
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty"""
        if self.is_empty():
            return None
        else:
            return self.list[len(self.list)]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty"""
        if self.is_empty():
            raise ValueError('List is empty')
        else:
            item = self.list[len(self.list)]
            self.list.remove(self.list[len(self.list)])
            return item

# implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
