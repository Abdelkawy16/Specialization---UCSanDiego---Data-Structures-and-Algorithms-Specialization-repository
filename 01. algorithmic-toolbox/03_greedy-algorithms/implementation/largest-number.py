def main():
    lst = list(map(int,input("Enter the numbers : ").split()))
    lst.sort(reverse=True)
    for i in lst:
        print(i, end='')

if __name__ == '__main__':
    main()
    