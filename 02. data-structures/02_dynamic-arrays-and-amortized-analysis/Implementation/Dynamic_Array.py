import ctypes

class dynamicArray():
    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._A = self._makeArray(self._capacity)

    def _makeArray(self, c):
        return (c * ctypes.py_object)()

    def pushBack(self, val):
        if self._size == self._capacity:
            _B = self._makeArray(2 * self._capacity)
            for i in range(self._size):
                _B[i] = self._A[i]
            self._A = _B
            self._capacity *= 2
        self._A[self._size] = val
        self._size += 1
    
    def Set(self, i, val):
        if i < 0 and i >= self._size:
            raise "Index out of range"
        self._A[i] = val

    def Get(self, i):
        if i < 0 and i >= self._size:
            raise "Index out of range"
        return self._A[i]
    
    def Remove(self, i):
        if i < 0 and i >= self._size:
            raise "Index out of range"
        for j in range(i, self._size - 1):
            self._A[j] = self._A[j + 1]
        self._size -= 1
    
    def Size(self):
        return self._size