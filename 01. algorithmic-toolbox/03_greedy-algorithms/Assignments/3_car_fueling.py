def main():
    x = [0]
    length = int(input())
    d = int(input())
    i = int(input())
    x += map(int, input().split()[0:i])
    x.append(length)
    n = len(x) - 2
    print(minRefills(x, n, d))

def minRefills(x, n, d):
    if d >= x[-1]:
        return 0
    numRefills = 0
    currentRefill = 0
    while currentRefill <= n:
        lastRefill = currentRefill
        while currentRefill <= n and (x[currentRefill+1] - x[lastRefill]) <= d:
            currentRefill += 1
        if currentRefill <= n and x[currentRefill+1] - x[currentRefill] > d:
            return -1
        if currentRefill <= n:
            numRefills += 1
    return numRefills


if __name__ == "__main__":
    main()