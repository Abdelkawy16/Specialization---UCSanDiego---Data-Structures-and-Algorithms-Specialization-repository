from priorityQueues import SortedPriorityQueue, UnsortedPriorityQueue
from priorityQueuesHeap import HeapPriorityQueue
from DisjointSets import disjointSet, disjointSet2, disjointSet3

def main():
    s = SortedPriorityQueue()
    s.Insert(5)
    s.Insert(4)
    s.Insert(10)
    s.Insert(7)
    print(s.ExtractMax())   #10

    us = UnsortedPriorityQueue()
    us.Insert(5)
    us.Insert(4)
    us.Insert(10)
    us.Insert(7)
    print(us.ExtractMax())   #10

    H = HeapPriorityQueue()
    H.Insert(5) #[5]
    H.Insert(7) #[7, 5]
    H.Insert(4) #[7, 4, 5]
    H.Insert(9) #[9, 7, 4, 5]
    H.Insert(3) #[9, 7, 4, 5, 3]
    H.Insert(8) #[9, 7, 8, 5, 3, 4]
    H.Insert(6) #[9, 7, 8, 5, 3, 4, 6]
    print(H.ExtractMax())   #9
    H.Remove(0) #8
    H.ChangePriority(4, 15) #[15, 7, 6, 4, 5]
    print(H.ExtractMax())   #15

    dj = disjointSet(5)
    dj.MakeSet(1)
    dj.MakeSet(5)
    dj.MakeSet(3)
    dj.MakeSet(4)
    dj.MakeSet(2)
    dj.Union(1, 2)
    print(dj._smallest) #[1, 1, 3, 4, 5]
    dj.Union(5, 4)
    print(dj._smallest) #[1, 1, 3, 4, 4]

    dj2 = disjointSet2(5)
    dj2.MakeSet(1)
    dj2.MakeSet(5)
    dj2.MakeSet(3)
    dj2.MakeSet(4)
    dj2.MakeSet(2)
    dj2.Union(1, 3) #{1, 3}
    print(dj2._smallest[0]._element) #1
    print(dj2._smallest[0]._next._element) #3
    print(dj2._smallest[0]._next._prev._element) #1
    dj2.Union(3, 5) #{1, 3, 5}
    print(dj2._smallest[0]._element) #1
    print(dj2._smallest[0]._next._element) #3
    print(dj2._smallest[0]._next._next._element) #5

    dj3 = disjointSet3(5)
    dj3.MakeSet(1)
    dj3.MakeSet(5)
    dj3.MakeSet(3)
    dj3.MakeSet(4)
    dj3.MakeSet(2)  #_parent[1, 2, 3, 4, 5] _rank[0, 0, 0, 0, 0]
    dj3.Union(1, 3) #_parent[3, 2, 3, 4, 5] _rank[0, 0, 1, 0, 0]
    dj3.Union(3, 5) #_parent[3, 2, 3, 4, 3] _rank[0, 0, 1, 0, 0]
    

if __name__ == '__main__':
    main()
    