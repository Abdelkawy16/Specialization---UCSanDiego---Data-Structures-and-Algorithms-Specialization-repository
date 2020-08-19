def main():
    while True:
        amount = int(input())
        if amount >= 1 and amount <= 1000:
            break
        else:
            print("please enter another number between 0 and 45: ", end='')
    print(money_change(amount))

def money_change(amount):
    coins = 0
    while amount > 0:
        if amount >= 10:
            coins += 1
            amount -= 10 
        elif amount >= 5:
            coins += 1
            amount -= 5 
        else:
            coins += 1
            amount -= 1
    return coins 

if __name__ == '__main__':
    main()
    