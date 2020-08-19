def main():
    inp = int(input())
    print(DPChange(inp, [4, 3, 1]))

#Dynamic problem algorithm
def DPChange(money, coins):
    MinNumCoins = [None for i in range(money + 1)]
    MinNumCoins[0] = 0
    for i in range(1, money + 1):
        for coin in coins:
            if coin > i:
                continue
            if MinNumCoins[i] == None or i >= coin:
                NumCoins = MinNumCoins[i - coin] + 1
                if MinNumCoins[i] == None or NumCoins < MinNumCoins[i]:
                    MinNumCoins[i] = NumCoins
    return MinNumCoins[money]

if __name__ == '__main__':
    main()
    