def main():
    A = [5,7,1,9,3,6,0]
    print(SelectionSort(A))
    print(MergeSort(A))
    print(CountSort(A))
    
def SelectionSort(A):
    for i in range(len(A)):
        minIndex = i
        for j in range(i + 1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        A[i], A[minIndex] = A[minIndex], A[i]    
    return A  

#Divide and Conqure Algorithm
def MergeSort(A):
    if len(A) == 1:
        return A
    mid = int(len(A)/2)
    # First Half
    B = MergeSort(A[0: mid])
    # Second Half
    C = MergeSort(A[mid:])
    # merge two sorted arrays
    result = Merge(B, C)
    return result

def Merge(B, C):
    result = [None for i in range(len(B)+len(C))]
    k = 0
    i = 0
    j = 0
    while i < len(B) and j < len(C):
        if B[i] < C[j]:
            result[k] = B[i]
            k += 1
            i += 1
        else:
            result[k] = C[i]
            k += 1
            j += 1
    # Store remaining elements
    while i < len(B):
        result[k] = B[i]
        k += 1
        i += 1
    while j < len(C):
        result[k] = C[j]
        k += 1
        j += 1
    return result

def CountSort(A):
    count = [0 for i in range(max(A) + 1)]
    for i in range(len(A)):
        count[A[i]] += 1
    pos = [0 for i in range(max(A) + 1)]
    for j in range(max(A) + 1):
        pos[j] = pos[j - 1] + count[j]
    output = [0 for i in range(len(A))]
    for i in range(len(A)):
        output[pos[A[i]] -1] = A[i]
        #pos[A[i]] += 1
    return output


if __name__ == "__main__":
    main()
    