from SinglyLinkedLists import SinglyLinkedList
#Implemented with array
class QueueArray():
    def __init__(self, _capacity):
        self._capacity = _capacity
        self._queueArray = [None] * self._capacity
        self._read = 0
        self._write = 0
    
    def Empty(self):
        return self._read == self._write and self._queueArray[self._write] == None
    
    def enqueue(self, element):
        if self._read - self._write == 1:
            raise "ERROR"
        if self._write == self._capacity - 1 and self._read == 0 and self._queueArray[self._write] != None:
            raise "Use larger Array"
        self._queueArray[self._write] = element
        if self._write == self._capacity - 1:
            self._write = 0
        else:
            self._write += 1
        
    def dequeue(self):
        if self.Empty():
            raise "Queue is empty"
        temp = self._queueArray[self._read]
        self._queueArray[self._read] = None
        if self._read == (self._capacity - 1):
            self._read = 0
        else:
            self._read += 1
        return temp

#Implemented with SinglyLinkedList
class LinkedQueue():
    def __init__(self):
        self._linkedQueue = SinglyLinkedList()
    
    def Empty(self):
        return self._linkedQueue._size == 0

    def enqueue(self, element):
        self._linkedQueue.PushBack(element)

    def dequeue(self):
        if self._linkedQueue._size == 0:
            raise "Queue is empty"
        temp = self._linkedQueue._head._element
        self._linkedQueue.PopFront()
        return temp