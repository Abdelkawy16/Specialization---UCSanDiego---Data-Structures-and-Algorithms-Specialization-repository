def main():
    n = int(input())
    segments = [[] for i in range(n)]
    for i in range(n):
        segments[i] += map(int, input().split())
    optimal_points(segments)

def optimal_points(segments):
    segments.sort(key = lambda i: i[1])
    print(segments)
    points = []
    i = 0 
    while i < len(segments):
        L, R = segments[i][0], segments[i][1]
        signTime = R
        i += 1
        while i < len(segments) and segments[i][0] <= R:
            if segments[i][1] < signTime:
                signTime = segments[i][1]
            i += 1
        points.append(signTime)
    print(len(points))
    print(" ".join([str(i) for i in points]))

if __name__ == "__main__":
    main()