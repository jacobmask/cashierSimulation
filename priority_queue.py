### File: priority_queue.py
from binheap import BinHeap

class PriorityQueue:
    def __init__(self):
        self._heap = BinHeap()

    def isEmpty(self):
        return self._heap.isEmpty()

    def enqueue(self, item):
        self._heap.insert(item)

    def dequeue(self):
        return self._heap.delMin()

    def peek(self):
        return self._heap.peekMin()

    def size(self):
        return self._heap.size()

    def __str__(self):
        return str(self._heap)
    
class PriorityQueueEntry:
    def __init__(self,priority,value):
        self.priority = priority
        self.val = value

    def getPriority(self):
        return self.priority

    def getValue(self):
        return self.val

    def setValue(self, newValue):
        self.val = newValue

    def __lt__(self,other):
        if self.priority < other.priority:
            return True
        else:
            return False

    def __gt__(self,other):
        if self.priority > other.priority:
            return True
        else:
            return False
        
    def __hash__(self):
        return self.key

import unittest

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()
        self.pq.enqueue(PriorityQueueEntry(5,'a'))                               
        self.pq.enqueue(PriorityQueueEntry(9,'d'))                  
        self.pq.enqueue(PriorityQueueEntry(1,'x'))
        self.pq.enqueue(PriorityQueueEntry(2,'y'))
        self.pq.enqueue(PriorityQueueEntry(3,'z'))

    def testInsert(self):
        assert self.pq.size() == 5

    def testPeek(self):
        assert self.pq.peek().getValue() == 'x'
        assert self.pq.peek().getValue() == 'x'
        assert self.pq.peek().getValue() == 'x'
        assert self.pq.peek().getValue() == 'x'

    def testDelmin(self):
        assert self.pq.dequeue().getValue() == 'x'
        assert self.pq.dequeue().getValue()  == 'y'
        assert self.pq.dequeue().getValue()  == 'z'
        assert self.pq.dequeue().getValue()  == 'a'

    def testMixed(self):
        myPQ = PriorityQueue()
        myPQ.enqueue(9)
        myPQ.enqueue(1)
        myPQ.enqueue(5)
        assert myPQ.dequeue() == 1
        myPQ.enqueue(2)
        myPQ.enqueue(7)
        assert myPQ.dequeue() == 2
        assert myPQ.dequeue() == 5

    def testDupes(self):
        myPQ = PriorityQueue()
        myPQ.enqueue(9)
        myPQ.enqueue(1)
        myPQ.enqueue(8)
        myPQ.enqueue(1)
        assert myPQ.size() == 4
        assert myPQ.dequeue() == 1
        assert myPQ.dequeue() == 1
        assert myPQ.dequeue() == 8

##    def testBuildHeap(self):
##        myPQ = priorityQueue()
##        myPQ.buildHeap([9,5,6,2,3])
##        f = myPQ.dequeue()
##        print("f = ", f)
##        assert f == 2
##        assert myPQ.dequeue() == 3
##        assert myPQ.dequeue() == 5
##        assert myPQ.dequeue() == 6
##        assert myPQ.dequeue() == 9                        
        
if __name__ == '__main__':
##    d = {}
##    d[PriorityQueueEntry(1,'z')] = 10
##    unittest.main()
    suite = unittest.makeSuite(TestPriorityQueue)
    unittest.TextTestRunner().run(suite)
    
        
