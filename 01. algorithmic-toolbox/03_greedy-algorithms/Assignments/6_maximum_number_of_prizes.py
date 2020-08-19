def main():
    n = int(input())
    max_num_of_prize(n)

def max_num_of_prize(n):
    i = 1
    Sum = 0
    Nums = []
    while i + Sum <= n:
        Sum += i
        Nums.append(i)
        i += 1
    Nums[-1] += n - Sum
    print(len(Nums))
    print(*Nums)

if __name__ == '__main__':
    main()
    