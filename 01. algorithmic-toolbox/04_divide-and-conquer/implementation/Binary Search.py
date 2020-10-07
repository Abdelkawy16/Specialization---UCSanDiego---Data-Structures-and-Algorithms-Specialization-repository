def main():
    lst = list(map(int,input().split()))
    item = int(input())
    print(binary_search(lst, item))

def binary_search(lst, item):
    lst.sort()
    low = 0
    high = len(lst) - 1
    while low < high:
        mid = low + (high - low) // 2
        if item == lst[mid]:
            return mid
        elif lst[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return low

if __name__ == '__main__':
    main()
