def main():
    print(EditDistance('distance', 'editing'))

# Computing edit distance
def EditDistance(A, B):
    distances = [i for i in range(len(A) + 1)]
    for j, c2 in enumerate(B):
        _distances = [j+1]
        for i, c1 in enumerate(A):
            if c1 == c2:
                _distances.append(distances[i])
            else:
                _distances.append(1 + min((distances[i], distances[i + 1], _distances[-1])))
        distances = _distances
    return distances[-1]

# Reconstructing an optimal alignment
def OutputAlignment(A, B):

if __name__ == '__main__':
    main()
    