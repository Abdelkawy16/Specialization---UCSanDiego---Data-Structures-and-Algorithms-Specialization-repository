import random

def maxProductFast(n, lst):
    global fast
    max_index1 = -1
    for i in range(n):
        if max_index1 == -1 or lst[i] > lst[max_index1]:
            max_index1 = i

    max_index2 = -1
    for i in range(n):
        if i != max_index1 and (max_index2 == -1 or lst[i] > lst[max_index2]):
            max_index2 = i
    fast = lst[max_index1] * lst[max_index2]
    return fast

def maxProduct(n, lst):
    global result
    for i in range(n):
        for j in range(i+1, n):
            if  lst[i]*lst[j] > result:
                result = lst[i]*lst[j]
    return result

result = 0
fast = 0

while result == fast:
    if __name__ == '__main__':
        n = (random.randint(2, 11))
        result = 0
        fast = 0
        lst = list(random.randint(0, 99999) for r in range(n))
        assert len(lst) == n, "Wrong Answer"
        result = maxProduct(n, lst)
        fast = maxProductFast(n, lst)
        print(fast, result, "OK")
    else:
        print("Wrong Answer")
