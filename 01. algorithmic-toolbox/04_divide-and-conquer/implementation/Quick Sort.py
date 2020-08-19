import random

def main():
    A = list(map(int,input().split()))
    print(QuickSort(A, 0, len(A) - 1))
    print(RandomizedQuickSort(A, 0, len(A) - 1))

def QuickSort(A, l, r):
    if l >= r:
        return
    m = partition(A, l, r)
    QuickSort(A, l, m)
    QuickSort(A, m + 1, r)
    return A

def RandomizedQuickSort(A, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    A[k], A[l] = A[l], A[k]
    m = partition(A, l, r)
    RandomizedQuickSort(A, l, m)
    RandomizedQuickSort(A, m + 1, r)
    return A

def partition(A, l, r):
    j = l
    x = A[l]
    for i in range(l + 1, r + 1):
        if A[i] <= x :
            j += 1
            A[i], A[j] =A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

if __name__ == '__main__':
    main()