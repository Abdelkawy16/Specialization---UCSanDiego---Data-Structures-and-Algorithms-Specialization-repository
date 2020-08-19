def main():
    while True:
        a, b = map(int, input().split())
        if (a >= 1 and a <= 2 * 10**9) and (b >= 1 and b <= 2 * 10**9):
            break
        else:
            print("please enter numbers between 1 and 2*10^9: ", end='')

    gcd = GCD(a, b)
    print(gcd)

def GCD(a, b):
    if b == 0:
        return a
    a0 = a % b
    return GCD(b, a0)

if __name__ == "__main__":
    main()
