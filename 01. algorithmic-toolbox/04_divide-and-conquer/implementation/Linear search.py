def main():
    lst = list(map(int,input().split()))
    item = int(input())
    print(linear_search(lst, item))

def linear_search(lst, item):
    index = None
    for i in range(len(lst)):
        if lst[i] == item:
            index = i
            break
    if index == None:
        return "NOT_FOUND"
    return index

if __name__ == '__main__':
    main()
    