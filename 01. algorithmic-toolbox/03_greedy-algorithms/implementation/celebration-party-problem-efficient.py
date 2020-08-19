def main():
    lst = list(map(int,input("Enter the students' age : ").split()))
    lst.sort(reverse=False)
    n = pointsCoverSorted(lst)
    print(n)
  
def pointsCoverSorted(lst):
    R = []
    i = 0
    while i <= len(lst) - 1:
        [l, r] = [lst[i], lst[i] + 1]
        R.append([l, r])
        i += 1
        while i <= len(lst) - 1 and lst[i] <= r:
              i += 1
    return R


if __name__ == "__main__":
    main()
