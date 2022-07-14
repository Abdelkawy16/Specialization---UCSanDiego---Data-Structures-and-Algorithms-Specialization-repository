#Uses python3

import sys

def dfs(v, visited, adj, order):
    #write your code here
    visited[v] = True

        # Recur for all the vertices adjacent to this vertex
    for i in adj[v]:
        if visited[i] == False:
            dfs(i, visited, adj, order)

    order.append(v)


def toposort(adj):
    used = [0] * len(adj)
    order = []
    #write your code here
    visited = [False for _ in range(len(adj))]
    for i in range(len(adj)):
        if visited[i] == False:
            dfs(i, visited, adj, order)
            
    return order[::-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

