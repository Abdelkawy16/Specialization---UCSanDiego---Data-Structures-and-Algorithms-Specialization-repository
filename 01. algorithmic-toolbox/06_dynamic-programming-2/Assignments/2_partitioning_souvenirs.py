def main():
    n = int(input())
    itemWeights = [int(i) for i in input().split()][0: n]
    totalWeight = sum(itemWeights)
    if n < 3: 
        print('0')
    elif totalWeight % 3 != 0: 
        print('0')
    else:
        partitions(totalWeight // 3, n, itemWeights)

# Discrete Knapsack problem without repetition
def partitions(W, n, items):
    count = 0 
    value = [[0 for j in range(n + 1)] for i in range(W + 1)]
    for i in range(1, W + 1):
        for j in range(1, n + 1):
            value[i][j] = value[i][j - 1]
            if items[j-1]<=i:
                val = value[i-items[j - 1]][j - 1] + items[j - 1]
                if val > value[i][j]:
                    value[i][j] = val
            if value[i][j] == W:
                count += 1
    if count < 3:
        print('0')
    else:
        print('1')

if __name__ == '__main__':
    main()