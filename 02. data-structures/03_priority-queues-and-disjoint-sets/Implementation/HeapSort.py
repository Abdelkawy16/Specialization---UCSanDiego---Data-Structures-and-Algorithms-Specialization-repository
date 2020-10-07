def main():
    Arr = [4, 5, 7, 2, 3, 1]
    print(HeapSort(Arr))    #[1, 2, 3, 4, 5, 7]

''' def HeapSort1(Arr):
    hpArr = HeapPriorityQueue()
    for i in range(len(Arr)):
        hpArr.Insert(Arr[i])
    for i in range(len(Arr) - 1, -1, -1):
        Arr[i] = hpArr.ExtractMax()
    return Arr '''

def LeftChild(i):
    return 2 * i + 1

def RightChild(i):
    return 2 * i + 2

def SiftDown(Arr, n, i):
    maxIndex = i
    l = LeftChild(i)
    if l <= n - 1 and Arr[l] > Arr[maxIndex]:
        maxIndex = l
    r = RightChild(i)
    if r <= n - 1 and Arr[r] > Arr[maxIndex]:
        maxIndex = r
    if i != maxIndex:
        Arr[i], Arr[maxIndex] = Arr[maxIndex], Arr[i]
        SiftDown(Arr, n, maxIndex)
    
def buildHeap(Arr):
    size = len(Arr)
    for i in range(size // 2 - 1, -1, -1):
        SiftDown(Arr, size, i)
    
def HeapSort(Arr):
    size = len(Arr)
    buildHeap(Arr)
    for i in range(size - 1, 0, -1):
        Arr[0], Arr[i] = Arr[i], Arr[0]
        SiftDown(Arr, i, 0)
    return Arr

if __name__ == '__main__':
    main()