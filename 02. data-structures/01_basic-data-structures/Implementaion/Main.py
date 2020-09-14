from SinglyLinkedLists import SinglyLinkedList
from DoublyLinkedLists import DoublyLinkedList
from Stack import LinkedStack, StackArray
from Queues import LinkedQueue, QueueArray

def main():
    # SinglyLinkedList
    l1 = SinglyLinkedList()
    l1.PushFront(5)
    l1.PushBack(6)
    l1.AddAfter(l1._head._next, 9) #PushBack
    l1.printList()
    print(l1._isEmpty())   #false
    l1.PopBack()
    l1.PopFront()
    l1.PopFront()
    print(l1._isEmpty())   #true

    # DoublyLinkedList
    l2 = DoublyLinkedList()
    l2.PushFront(5)
    l2.PushBack(6)
    l2.AddAfter(l2._head._next, 9) #PushBack
    l2.AddBefore(l2._head, 4)   #PushFront
    l2.printList()
    print(l2._isEmpty())   #false
    l2.PopBack()
    l2.PopFront()
    l2.PopFront()
    l2.PopBack()
    print(l2._isEmpty())   #true

    # Stack
    s1 = LinkedStack()
    s1.push(5)
    print(s1.top()) #5
    s1.push(6)
    print(s1.top()) #6
    s1.push(7)
    s1.pop()
    s1.pop()
    print(s1.top()) #5

    # Queue Linked List
    Q1 = LinkedQueue()
    Q1.enqueue(5)
    Q1.enqueue(6)
    print(Q1.Empty())    #false
    print(Q1.dequeue()) #5
    print(Q1.dequeue()) #6
    print(Q1.Empty())    #true
    
    #QueueArray
    Q2 = QueueArray(3)
    Q2.enqueue(1)
    Q2.enqueue(2)
    Q2.enqueue(3)
    print(Q2.dequeue()) #1
    print(Q2.dequeue()) #2
    Q2.enqueue(4)
    print(Q2.dequeue()) #3
    print(Q2.Empty()) #False
    print(Q2.dequeue()) #4
    print(Q2.Empty()) #TRue



if __name__ == "__main__":
    main()