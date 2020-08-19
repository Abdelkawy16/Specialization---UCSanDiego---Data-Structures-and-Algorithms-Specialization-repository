# Uses python3
import sys

def get_majority_element(A, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return A[left]
    #write your code here
    mid = (right + left - 1) // 2
    lElement = get_majority_element(A, left, mid + 1)
    rElement = get_majority_element(A, mid + 1, right)

    lCount = 0
    for i in range(left, right):
        if A[i] == lElement:
            lCount += 1
    if lCount > (right - left) // 2:
        return lElement 

    rCount = 0
    for i in range(left, right):
        if A[i] == rElement:
            rCount += 1
    if rCount > (right - left) // 2:
        return rElement 

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
