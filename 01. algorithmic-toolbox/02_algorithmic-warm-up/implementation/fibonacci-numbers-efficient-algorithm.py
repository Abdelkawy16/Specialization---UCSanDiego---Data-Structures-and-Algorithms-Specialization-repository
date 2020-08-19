def main():
    inp = int(input("enter the nth fibonacci number: "))
    fib = fibList(inp)
    print(fib)

def fibList(n):
    lst = [0, 1]
    if n <= 1:
        return n
    for i in range(2, n + 1):
        lst.append(lst[i-1] + lst[i-2]) 
    return lst[n]

if __name__ == "__main__":
    main()
