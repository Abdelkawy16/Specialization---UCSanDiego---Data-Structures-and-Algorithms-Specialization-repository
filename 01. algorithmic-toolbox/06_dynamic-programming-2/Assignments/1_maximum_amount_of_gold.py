def main():
    W, n = map(int, input().split())
    # (amount, value)
    A = [(i, i) for i in list(map(int, input().split()))[0: n]]
    print(knapsackWithoutRepetitions(W, A))

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

if __name__ == '__main__':
    main()
    