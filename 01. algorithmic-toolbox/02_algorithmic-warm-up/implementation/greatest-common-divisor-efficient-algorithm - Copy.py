def main():
    a, b = map(int, input().split())
    gcd = euclidGCD(a, b)
    print(gcd)

def euclidGCD(a, b):
    if b == 0:
        return a
    a0 = a % b
    return euclidGCD(b, a0)

if __name__ == "__main__":
    main()
