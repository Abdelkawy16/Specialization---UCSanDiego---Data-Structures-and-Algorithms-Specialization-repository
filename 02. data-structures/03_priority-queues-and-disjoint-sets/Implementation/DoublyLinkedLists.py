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
        
    def Push(self, element):
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

    def printList(self): 
        temp = self._head 
        while temp != None: 
            print(temp._element) 
            temp = temp._next