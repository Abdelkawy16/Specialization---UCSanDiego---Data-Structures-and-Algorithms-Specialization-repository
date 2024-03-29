# Uses python3

import sys


def number_of_components(adj):
    result = 0
    visited = [False for _ in range(len(adj))]

    def dfs(x):
        visited[x] = True
        for w in adj[x]:
            if visited[w] is False:
                dfs(w)
    for i in range(0, len(visited)):
        if visited[i] == False:
            dfs(i)
            result += 1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
