class SinglyLinkedList():
    class _Node():
        def __init__(self, _element):
            self._element = _element
            self._next = None
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def _isEmpty(self):
        return self._size == 0
    
    def PushFront(self, element):
        self._head = self._Node(element)
        self._head._next = self._head
        self._size += 1
        if self._tail == None:
            self._tail = self._head
    
    def PopFront(self):
        if self._head == None:
            raise "List is empty"
        self._head = self._head._next
        self._size -= 1
        if self._head == None:
            self._tail = None
        
    def PushBack(self, element):
        node = self._Node(element)
        if self._tail == None:
            self._tail = node
            self._head = self._tail
            self._size += 1
        else:
            self._tail._next = node
            self._tail = node
            self._size += 1
    
    def PopBack(self):
        #EmptyList
        if self._head == None:
            raise "List is empty"
        #OneElement
        if self._head == self._tail:
            self._tail = None
            self._head = self._tail
            self._size -= 1
        else:
            p = self._head
            while p._next._next != None:
                p = p._next
            p._next = None
            self._tail = p
            self._size -= 1
        
    def AddAfter(self, node, element):
        if node == None:
            raise "The given node must inLinkedList!"
        node2 = self._Node(element)
        node2._next = node._next
        node._next = node2
        self._size += 1
        if self._tail == node:
            self._tail = node2
    
    def printList(self): 
        temp = self._head 
        while (temp): 
            print(temp._element) 
            temp = temp._next
