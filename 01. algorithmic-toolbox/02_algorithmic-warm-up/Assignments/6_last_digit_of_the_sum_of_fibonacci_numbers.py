def main():
    while True:
        inp = int(input())
        if inp >= 0 and inp <= 10**14:
            break
        else:
            print("please enter another number between 0 and 10^14: ", end='')
    
    fib = fibList(inp)
    print(fib)

def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m 
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1

def fibList(n):
    result = 1
    previous = 0
    current = 1
    if n <= 1:
        return n
    n %= pisanoPeriod(10)
    for i in range(2, n + 1):
        previous, current = current, (previous + current) % 10
        result += current
    return result % 10

if __name__ == "__main__":
    main()
