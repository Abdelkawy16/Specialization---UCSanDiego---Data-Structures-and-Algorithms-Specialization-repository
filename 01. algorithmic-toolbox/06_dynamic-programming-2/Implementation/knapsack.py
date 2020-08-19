def main():
    #(amount, value)
    A = [(2, 9), (4, 16), (3, 14), (6, 30)]
    W = 10
    HT = [0 for i in range(W + 1)]  # Hash table
    print(knapsackWithRepetitions(W, A))
    print(knapsackWithoutRepetitions(W, A))
    print(Knapsack(W, A, HT))

# knapsack-with-repetitions
def knapsackWithRepetitions(W, A):
    values = [0 for i in range(W + 1)]
    for w in range(1, W + 1):
        for i in range(0, len(A)):
            if A[i][0] <= w:
                val = values[w - A[i][0]] + A[i][1]
                if val > values[w]:
                    values[w] = val
    return values[W]
            

# knapsack-without-repetitions
def knapsackWithoutRepetitions(W, A):
    values = [[0 for j in range(len(A))] for i in range(W + 1)]
    for i in range(0, len(A)):
        for w in range(0, W + 1):
            values[w][i] = values[w][i - 1]
            if A[i][0] <= w:
                val = values[w - A[i][0]][i - 1] + A[i][1]
                if val > values[w][i]:
                    values[w][i] = val
    return values[W][len(A) - 1]

# Memoization
def Knapsack(W, A, HT):
    for i in HT:
        if W == HT[W]:
            return HT[W]
    # (1, len(A)) knapsack Without Repetitions
    # (0, len(A)) knapsack With Repetitions
    for i in range(1, len(A)):
        if A[i][0] <= W:
            val = Knapsack(W - A[i][0], A, HT) + A[i][1]
            if val > HT[W]:
                HT[W] = val
    return HT[W]

if __name__ == '__main__':
    main()
    
