def main():
    a, b = map(int, input().split())
    gcd = naiveGCD(a, b)
    print(gcd)

def naiveGCD(a, b):
    best = 0
    for d in range(1, min(a,b)+1):
        if b % d == 0 and a % d == 0:
            best = d
    return best

if __name__ == "__main__":
    main()
