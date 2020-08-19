def main():
    n = 4
    A = [4, 3, 2, 1]
    B = [1, 2, 3, 4]
    print(multPoly(A, B, n))
    print(multPoly2(A, B, n, 0, 0))

def multPoly(A, B, n):
    product = [0 for i in range(2 * n - 1)]
    for i in range(n):
        for j in range(n):
            product[i + j] += A[i] * B[j]
    return product

# Divide and Conqure Algorithm
def multPoly2(A, B, n, a, b):
    product = [0 for i in range(2 * n - 1)]
    if n == 1:
        product[0] = A[a] * B[b]
        return product
    # First Half (A0, B0)
    product[0: n - 1] = multPoly2(A, B, int(n/2), a, b)
    # Second Half (A1, B1)
    product[n: 2 * n - 1] = multPoly2(A, B, n -int(n/2), a + int(n/2), b + int(n/2))

    A0B1 = multPoly2(A, B, n - int(n/2), a, b + int(n/2))
    A1B0 = multPoly2(A, B, n - int(n/2), a + int(n/2), b)

    product[int(n/2): n + int(n/2) - 1] = [a + b for a, b in zip(product[int(n/2): n + int(n/2) - 1], [a + b for a, b in zip(A0B1, A1B0)])]
    return product

if __name__ == '__main__':
    main()