### File: queue_text.py
class QueueText(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        resultStr = "(rear)"
        for item in self.items:
            resultStr = str(item) + " " + resultStr
        resultStr = "(front) " + resultStr
        return resultStr
    
        
