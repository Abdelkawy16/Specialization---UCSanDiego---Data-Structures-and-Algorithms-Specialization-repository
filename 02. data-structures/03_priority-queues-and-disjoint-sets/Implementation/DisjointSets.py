from DoublyLinkedLists import DoublyLinkedList

#NAIVE
#using List
class disjointSet:
    def __init__(self, size):
        self._smallest = [None] * size

    def MakeSet(self, i):
        self._smallest[i - 1] = i

    def Find(self, i):
        return self._smallest[i - 1]
    
    def Union(self, i, j):
        i_id = self.Find(i)
        j_id = self.Find(j)
        if i_id == j_id:
            return
        m = min(j_id, i_id)
        for x in range(len(self._smallest)):
            if self._smallest[x] == max(j_id, i_id):
                self._smallest[x] = m

#using linkedList
class disjointSet2:
    def __init__(self, size):
        self._smallest = [None] * size

    def MakeSet(self, i):
        lnkd = DoublyLinkedList()
        lnkd.Push(i)
        self._smallest[i - 1] = lnkd._tail

    def FindHead(self, i):
        s = self._smallest[i - 1]
        while s._prev:
            s = s._prev
        return s

    def FindTail(self, i):
        s = self._smallest[i - 1]
        while s._next:
            s = s._next
        return s
    
    def Union(self, i, j):
        i_id = self.FindHead(i)
        j_id = self.FindHead(j)
        if i_id == j_id:
            return
        i_id = self.FindTail(i)
        i_id._next = j_id
        j_id._prev = i_id      
    
#EFFECIENT
#using tree
class disjointSet3:
    def __init__(self, size):
        self._parent = [None] * size
        self._rank = [None] * size

    def MakeSet(self, i):
        self._parent[i - 1] = i
        self._rank[i - 1] = 0

    def Find(self, i):
        ''' while i != self._parent[i - 1]:
            i = self._parent[i - 1]
        return i '''
        #path compression
        if i != self._parent[i - 1]:
            self._parent[i - 1] = self.Find(self._parent[i - 1])
        return self._parent[i - 1]
    
    def Union(self, i, j):
        i_id = self.Find(i)
        j_id = self.Find(j)
        if i_id == j_id:
            return
        if self._rank[i_id - 1] > self._rank[j_id - 1]:
            self._parent[j_id - 1] = i_id
        else:
            self._parent[i_id - 1] = j_id
            if self._rank[i_id - 1] == self._rank[j_id - 1]:
                self._rank[j_id - 1] += 1