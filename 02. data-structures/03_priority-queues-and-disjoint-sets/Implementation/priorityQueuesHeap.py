class HeapPriorityQueue:
    def __init__(self):
        self._data = []
    
    def Parent(self, i):
        return int((i - 1) / 2)
    
    def LeftChild(self, i):
        return 2 * i + 1
    
    def RightChild(self, i):
        return 2 * i + 2
    
    def SiftUp(self, i):
        while i > 0 and self._data[self.Parent(i)] < self._data[i]:
            self._data[self.Parent(i)] , self._data[i] = self._data[i], self._data[self.Parent(i)]
            i = self.Parent(i)
    
    def SiftDown(self, i):
        maxIndex = i
        l = self.LeftChild(i)
        if l <= len(self._data) - 1 and self._data[l] > self._data[maxIndex]:
            maxIndex = l
        r = self.RightChild(i)
        if r <= len(self._data) - 1 and self._data[r] > self._data[maxIndex]:
            maxIndex = r
        if i != maxIndex:
            self._data[i], self._data[maxIndex] = self._data[maxIndex], self._data[i]
            self.SiftDown(maxIndex)
    
    def Insert(self, p):
        self._data.append(p)
        self.SiftUp(len(self._data) - 1)
    
    def ExtractMax(self):
        result = self._data[0]
        self._data[0] = self._data[-1]
        self._data.pop()
        self.SiftDown(0)
        return result
    
    def Remove(self, i):
        self._data[i] = float('inf')
        self.SiftUp(i)
        self.ExtractMax()
    
    def ChangePriority(self, i , p):
        oldP = self._data[i]
        self._data[i] = p
        if oldP < p:
            self.SiftUp(i)
        else:
            self.SiftDown(i) 
