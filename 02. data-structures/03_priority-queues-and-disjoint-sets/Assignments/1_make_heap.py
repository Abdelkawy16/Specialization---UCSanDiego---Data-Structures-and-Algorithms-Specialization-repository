# python3
def LeftChild(i):
    return 2 * i + 1

def RightChild(i):
    return 2 * i + 2

def SiftDown(swaps, Arr, n, i):
    minIndex = i
    l = LeftChild(i)
    if l <= n - 1 and Arr[l] < Arr[minIndex]:
        minIndex = l
    r = RightChild(i)
    if r <= n - 1 and Arr[r] < Arr[minIndex]:
        minIndex = r
    if i != minIndex:
        swaps.append((i, minIndex))
        Arr[i], Arr[minIndex] = Arr[minIndex], Arr[i]
        swaps = SiftDown(swaps, Arr, n, minIndex)
    return swaps
    
def buildHeap(Arr):
    swaps = []
    size = len(Arr)
    for i in range(size // 2 - 1, -1, -1):
        swaps = SiftDown(swaps, Arr, size, i)
    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = buildHeap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
