def main():
    while True:
        inp = int(input())
        if inp >= 0 and inp <= 10**7:
            break
        else:
            print("please enter another number between 0 and 10^7: ", end='')
    
    fib = fibList(inp)
    print(fib)

def fibList(n):
    previous = 0
    current = 1
    if n <= 1:
        return n
    for i in range(2, n + 1):
        previous, current = current, (previous + current) % 10 
    return current

if __name__ == "__main__":
    main()
