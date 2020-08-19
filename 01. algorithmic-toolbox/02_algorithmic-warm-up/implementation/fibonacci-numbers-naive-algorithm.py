def main():
    inp = int(input("enter the nth fibonacci number: "))
    fib = fibRecurs(inp)
    print(fib)

def fibRecurs(n):
    if n <= 1:
        return n
    else:
        return fibRecurs(n-1) + fibRecurs(n-2)

if __name__ == "__main__":
    main()