from itertools import product

def main():
    x = check_if_partition_possible(3, [1,2,5,4,6], 5)
    print(x)

# n is the number of children, k is the number of groups
# x are the coordinates (ages) of the children
# the function returns True if it is possible to split
# children into k gorups.
def check_if_partition_possible(k, x, n):
  for partition in product(list(range(k)), repeat=n):
    G = [[] for i in range(k)] 
    # prepare the groups, G[i] contains the coordinates of 
    # the children in the ith group
    for i in range(n):
      G[partition[i]].append(x[i])
    good = True
    for i in range(k):
      if len(G[i]) == 0 or max(G[i]) - min(G[i]) > 1:
        good = False
    if good:
      return True
  return False

if __name__ == "__main__":
    main()