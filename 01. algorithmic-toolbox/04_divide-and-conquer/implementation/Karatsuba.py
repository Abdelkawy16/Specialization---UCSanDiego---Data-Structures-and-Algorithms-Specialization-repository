def main():
    x = int(input("Enter 1st num: "))
    y = int(input("Enter 2nd num: "))
    mult = multiple(x, y)
    print(mult)

def multiple(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        maxLength = max(len(str(x)), len(str(y)))
        s = maxLength // 2
        a = x // 10**s
        b = x % 10**s
        c = y // 10**s
        d = y % 10**s
        f = multiple(a+b, c+d) - multiple(b, d) - multiple(a, c)
        return multiple(a, c)*10**(2*s) - multiple(b, d) - f*10**s

if __name__ == "__main__":
    main()
    