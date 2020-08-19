def main():
    W = 15
    #key = amount and value = value
    dic = {5:15, 6:12, 7:28}
    print(knapsack(W, dic))
    
def knapsack(W, dic):
    A = [0 for i in range(len(dic))]
    V = 0
    wv = []
    for key in dic:
        wv.append(dic[key]/key)
    wv.sort(reverse=True)
    for i in range(len(wv)):
        if W == 0:
            return (V, A)
        _amount = None
        index = 0
        for amount in dic:
            if _amount == None or (amount > 0 and (dic[amount]/amount) == max(wv)):
                _amount = amount
                index = list(dic.keys()).index(amount)
        a = min(W, _amount)
        V += a * (dic[_amount]/_amount)
        wv.remove(max(wv))
        A[index] += a
        W -= a
    return (V, A)



if __name__ == "__main__":
    main()