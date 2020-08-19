def main():
    print(GreedyChange(40))
    print(RecursiveChange(9, [6, 5, 1]))
    print(DPChange(32, [20, 8, 1]))

def GreedyChange(money):
    change = []
    while money > 0:
        if money >= 25:
            change.append(25)
            money -= 25
        elif money >= 10:
            change.append(10)
            money -= 10
        elif money >= 5:
            change.append(5)
            money -= 5
        else:
            change.append(1)
            money -= 1
    return change

def RecursiveChange(money, coins):
    if money == 0:
        return 0
    MinNumCoins = None
    for coin in coins:
        if money >= coin:
            NumCoins = RecursiveChange(money - coin, coins)
            if MinNumCoins == None or NumCoins + 1 < MinNumCoins:
                MinNumCoins = NumCoins + 1
    return MinNumCoins

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
    