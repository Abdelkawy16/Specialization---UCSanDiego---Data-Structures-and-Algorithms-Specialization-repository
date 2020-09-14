from SinglyLinkedLists import SinglyLinkedList
#Implemented with array
class StackArray():
    def __init__(self):
        self._stackArray = []
    
    def _isEmpty(self):
        return len(self._stackArray) == 0
    
    def push(self, element):
        self._stackArray.append(element)
    
    def top(self):
        if self._isEmpty:
            raise "stack is empty"
        return self._stackArray[-1]

    def pop(self):
        if self._isEmpty:
            raise "stack is empty"
        self._stackArray.pop()

#Implemented with SinglyLinkedList
class LinkedStack():
    def __init__(self):
        self._linkedStack = SinglyLinkedList()
    
    def push(self, element):
        self._linkedStack.PushBack(element)
    
    def top(self):
        if self._linkedStack._size == 0:
            raise "stack is empty"
        return self._linkedStack._tail._element

    def pop(self):
        if self._linkedStack._size == 0:
            raise "stack is empty"
        self._linkedStack.PopBack()