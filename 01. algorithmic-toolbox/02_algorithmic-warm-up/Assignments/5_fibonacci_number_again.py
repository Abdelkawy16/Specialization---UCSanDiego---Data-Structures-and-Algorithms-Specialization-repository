def main():
    while True:
        n, m = map(int, input().split())
        if (n >= 1 and n <= 10**14) and (m >= 2 and m <= 10**3):
            break
        else:
            print("please enter n between 1 and 10^14 and m between 2 and 10^3: ", end='')
    
    fib = fibList(n, m)
    print(fib)

def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m 
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1

def fibList(n, m):
    pisano_period = pisanoPeriod(m)
    n %= pisano_period
    previous = 0
    current = 1
    if n <= 1:
        return n
    for i in range(2, n + 1):
        previous, current = current % m, (previous + current) % m
    return current 

if __name__ == "__main__":
    main()
