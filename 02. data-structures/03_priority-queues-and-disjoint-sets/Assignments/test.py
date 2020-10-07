c = dict()
for n in range(8):
    c[n, 0] = 1
    c[n, n] = 1
    for k in range(1, n):
        c[n, k] = c[n - 1, k - 1] + c[n - 1, k]

from itertools import combinations_with_replacement
res = 0
for c in combinations_with_replacement("TBL", 4):
    print("".join(c))
    res += 1

print(res)