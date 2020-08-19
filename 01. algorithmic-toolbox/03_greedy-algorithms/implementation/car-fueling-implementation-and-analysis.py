def main():
    x = [0,1,2,3,4,5,6,7,8,9,10]
    l = 8
    n = len(x) - 2
    print(minRefills(x, n, l))

def minRefills(x, n, l):
    numRefills = 0
    currentRefill = 0
    while currentRefill <= n:
        lastRefill = currentRefill
        while currentRefill <= n and (x[currentRefill+1] - x[lastRefill]) <= l:
            currentRefill += 1
        if currentRefill == lastRefill:
            break
        if currentRefill <= n:
            numRefills += 1
    return numRefills


if __name__ == "__main__":
    main()