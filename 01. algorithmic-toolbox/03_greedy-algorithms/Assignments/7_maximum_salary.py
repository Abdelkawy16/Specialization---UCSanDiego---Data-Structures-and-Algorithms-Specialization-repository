def main():
    inp = int(input())
    lst = list(map(int,input().split()))[0:inp]
    max_salary(lst)

def IsGreater(i, max_digit):
    return int(str(i) + str(max_digit)) >= int(str(max_digit) + str(i))

def max_salary(lst):
    nums = []
    while len(lst) != 0:
        max_digit = max(lst)
        for i in lst:
            if i != max_digit and IsGreater(i, max_digit):
                max_digit = i
        nums.append(max_digit)
        lst.remove(max_digit)
        
    for i in nums:
        print(i, end='')

if __name__ == '__main__':
    main()
    