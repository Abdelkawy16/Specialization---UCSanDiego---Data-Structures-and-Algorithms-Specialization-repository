def main():
    operations = ['-', '+', '*', '-', '+']
    digits = [5, 8, 7, 4, 8, 9] 
    m = [[0 for i in range(len(digits))] for j in range(len(digits))]  #minimized values
    M = [[0 for i in range(len(digits))] for j in range(len(digits))]  #maximized values
    for x in range(len(digits)):
        m[x][x] = digits[x]
        M[x][x] = digits[x]
    for s in range(1, len(digits)):   #here's where I get confused
        for i in range(len(digits) - s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, operations, digits,m,M)
    print(M[0][len(digits)-1])

def MinAndMax(i, j, operations, digits, M, m):
    minV, maxV = None, None
    for k in range(i, j):
        a = result(M[i][k], operations[k], M[k + 1][j])
        b = result(M[i][k], operations[k], m[k + 1][j])
        c = result(m[i][k], operations[k], M[k + 1][j])
        d = result(m[i][k], operations[k], m[k + 1][j])
        try:
            minV = min(minV, a, b, c, d)
            maxV = max(maxV, a, b, c, d)
        except:
            minV = min(a, b, c, d)
            maxV = max(a, b, c, d)
    return (minV, maxV)

def result(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

if __name__ == '__main__':
    main()
    