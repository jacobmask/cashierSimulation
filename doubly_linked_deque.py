""" File: doubly_linked_deque.py
    Description:  Implements a doubly-linked version of a Deque using
    Node2@ay objects.
"""

from node2way import Node2Way

class Deque(object):
    def __init__(self):
        """ Constructs an empty Deque. """
        self._front = None
        self._rear = None
        self._size = 0

    def isEmpty(self):
        """ Return a Boolean indicating whether the Deque is empty or not."""
        return self._size == 0

    def addFront(self, item, clock):
        """ Adds item to the front of the Deque. """
        temp = Node2Way(item, clock)
        temp.setPrevious(self._front)
       
        if self._size == 0:
            self._rear = temp
        else:
            self._front.setNext(temp)
            
        self._front = temp
        self._size += 1

    def addRear(self, item, clock):
        """ Adds item to the front of the Deque. """
        temp = Node2Way(item, clock)
        temp.setPrevious(self._rear)

        if self._size == 0:
            self._front = temp
        else:
            self._rear.setNext(temp)

        self._rear = temp
        self._size += 1
        
        
    def removeFront(self):
        """ Removes and returns the front item of the Deque. """
        if self._size == 0:
            raise AttributeError("Cannot removeFront from an empty Deque")
        
        temp = self._front
        self._front = self._front.getPrevious()
        if self._size == 1:
            # removing only item which is the rear as well as the front item
            self._rear = None
        else:
            self._front.setNext(None)
        self._size -= 1
        
        return temp.getData()
    
    def removeRear(self):
        """ Removes and returns the rear item of the Deque. """
        # ADD CODE HERE
        if self._size == 0:
            raise AttributeError("Cannot remove rear from an empty Deque")

        temp = self._rear
        self._rear = self._rear.getPrevious()
        if self._size == 1:
            self._front = None
        else:
            self._rear.setNext(None)
        self._size -= 1

        return temp.getData()
    
    def peekFront(self):
        """ Returns the front item of the Deque without removing it. """
        if self._size == 0:
            raise AttributeError("Cannot peekFront from an empty Deque")
        return self._front.getData()

    def peekRear(self):
        """ Returns the rear item of the Deque without removing it. """
        # ADD CODE HERE
        if self._size == 0:
            raise AttributeError("Cannot peek rear from an empty Deque")
        return self._rear.getData()
        
    def size(self):
        """ Returns the number of items in the Deque. """
        return self._size

    def __str__(self):
        """ Returns a string representation of all items from rear to front."""
        resultStr = "(rear)"
        current = self._rear # point current at rear node
        while current != None: # while current points to a node
            resultStr = resultStr + " " + str(current.getData())
            current = current.getNext()  # move current to next node
        resultStr = resultStr + " (front)"
        return resultStr
    
        
