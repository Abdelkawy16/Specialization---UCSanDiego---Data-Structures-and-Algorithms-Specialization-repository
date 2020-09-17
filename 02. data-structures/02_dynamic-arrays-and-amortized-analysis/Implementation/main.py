from Dynamic_Array import dynamicArray

def main():
    # Dymnamic Array
    a = dynamicArray()
    a.pushBack(5)
    a.pushBack(6)
    a.pushBack(12)
    print(a.Get(1)) #6
    a.Set(1, 9)
    print(a.Get(1)) #9
    a.Remove(1)
    print(a.Get(1)) #12

if __name__ == '__main__':
    main()
    