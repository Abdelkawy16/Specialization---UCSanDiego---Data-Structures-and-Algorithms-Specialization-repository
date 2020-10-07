# Unsorted List
class UnsortedPriorityQueue:
    def __init__(self):
        self._data = []
    
    def Insert(self, e):
        self._data.append(e)
    
    def ExtractMax(self):
        maxItem = max(self._data)
        self._data.remove(maxItem)
        return maxItem
    
    # Sorted List
class SortedPriorityQueue:
    def __init__(self):
        self._data = []
    
    def _findIndex(self, e):
        #binary search
        """ low = 0
        high = len(self._data) - 1
        while low < high:
            mid = low + (high - low) // 2
            if e == self._data[mid]:
                return mid
            elif self._data[mid] > e:
                high = mid - 1
            else:
                low = mid + 1
        return low """
        #linear search
        for i in range(len(self._data)): 
            if self._data[i] > e: 
                index = i 
                break
        return index
                
    def Insert(self, e):
        if len(self._data) == 0 or e > self._data[-1]:
            self._data.append(e)
        else:
            index = self._findIndex(e)
            self._data = self._data[:index] + [e] + self._data[index:] 

    def ExtractMax(self):
        maxItem = self._data[-1]
        self._data.pop()
        return maxItem
