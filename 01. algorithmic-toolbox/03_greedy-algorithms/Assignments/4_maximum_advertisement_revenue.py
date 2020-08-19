def main():
    x,y = [],[]
    i = int(input())
    x += map(int, input().split()[0:i])
    y += map(int, input().split()[0:i])
    x.sort()
    y.sort()
    print(max_dot_product(x, y))

def max_dot_product(x, y):
    max_value = 0
    for i in range(len(x)):
        max_value += x[i] * y[i]
    return max_value

if __name__ == "__main__":
    main()