def main():
    while True:
        a, b = map(int, input().split())
        if (a >= 1 and a <= 10**7) and (b >= 1 and b <= 10**7):
            break
        else:
            print("please enter numbers between 1 and 10^7: ", end='')

    lcm = LCM(a, b)
    print(lcm)

def LCM(a, b):
    result = a * b
    for i in range(a * b, max(a, b) - 1, -max(a, b)):
        if i % a == 0 and i % b == 0:
            result = i
    return result

if __name__ == "__main__":
    main()
