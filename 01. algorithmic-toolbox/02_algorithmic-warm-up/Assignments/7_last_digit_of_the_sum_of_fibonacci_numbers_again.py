def main():
    while True:
        m, n = map(int, input().split())
        if (n >= 0 and n <= 10**14) and (m >= 0 and m <= 10**14):
            break
        else:
            print("please enter n between 0 and 10^14 and m between 0 and 10^14: ", end='')
    
    fib = fibList(m, n)
    print(fib)

def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m 
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1

def fibList(m, n):
    if m == 0 and n == 0:
        return 0
    n %= pisanoPeriod(10)
    m %= pisanoPeriod(10)
    if m > n:
        n += 60
    result = 0
    previous = 0
    current = 1
    if m <= 1:
        result = previous + current
    for i in range(2, n + 1):
        previous, current = current, (previous + current) % 10
        if i >= m: 
            result += current
    return result % 10

if __name__ == "__main__":
    main()
