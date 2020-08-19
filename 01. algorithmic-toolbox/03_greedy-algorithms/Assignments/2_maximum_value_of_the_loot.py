def main():
    n, W = map(int, input().split())
    #key = amount and value = value
    dic = {}
    for i in range(n):
        value, amount = map(int, input().split())
        dic[amount] = value
    print("{:.4f}".format(knapsack(W, dic)))
    
def knapsack(W, dic):
    V = 0
    wv = []
    for key in dic:
        wv.append(float(dic[key]/key))
    while (W > 0):
        _amount = None
        if len(dic) == 0:
            return V
        for amount in dic:
            if _amount == None or (amount > 0 and (float(dic[amount]/amount)) == max(wv)):
                _amount = amount
        a = min(W, _amount)
        V += float(a * float(dic[_amount]/_amount))
        wv.remove(max(wv))
        W -= a
        del dic[_amount]
    return V



if __name__ == "__main__":
    main()
