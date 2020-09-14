class DoublyLinkedList():
    class _Node():
        def __init__(self, _element):
            self._element = _element
            self._next = None
            self._prev = None
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def _isEmpty(self):
        return self._size == 0
    
    def PushFront(self, element):
        self._head, self._head._next = self._Node(element), self._head
        self._size += 1
        if self._tail == None:
            self._tail = self._head
    
    def PopFront(self):
        #EmptyList
        if self._head == None:
            raise "List is empty"
        self._head = self._head._next
        self._size -= 1
        if self._head == None:
            self._tail = None
        
    def PushBack(self, element):
        node2 = self._Node(element)
        #EmptyList
        if self._tail == None:
            self._tail = node2
            self._head = node2
            self._size += 1
        else:
            self._tail._next = node2
            node2._prev = self._tail
            self._tail = node2  
            self._size += 1
    
    def PopBack(self):
        #EmptyList
        if self._head == None:
            raise "List is empty"
        #OneElement
        if self._head == self._tail:
            self._tail = None
            self._head = None
            self._size -= 1
        #MoreThanOneElement
        else:
            self._tail = self._tail._prev
            self._tail._next = None
            self._size -= 1
        
    def AddAfter(self, node, element):
        if node == None:
            raise "The given node must in LinkedList!"
        node2 = self._Node(element)
        node2._next = node._next
        node2._prev = node
        node._next = node2
        self._size += 1
        if node2._next != None:
            node2._next._prev = node2
        if self._tail == node:
            self._tail = node2
        
    def AddBefore(self, node, element):
        if node == None:
            raise "The given node must in LinkedList!"
        node2 = self._Node(element)
        node2._next = node
        node2._prev = node._prev
        node._prev = node2
        self._size += 1
        if node2._prev != None:
            node2._prev._next = node2
        if self._head == node:
            self._head = node2

    def printList(self): 
        temp = self._head 
        while temp != None: 
            print(temp._element) 
            temp = temp._next