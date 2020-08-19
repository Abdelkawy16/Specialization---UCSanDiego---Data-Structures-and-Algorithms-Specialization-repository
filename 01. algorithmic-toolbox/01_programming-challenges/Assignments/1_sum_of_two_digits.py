def main():
    try:
        inp = input()
        token = inp.split()
        a = int(token[0])
        b = int(token[1])
        print(a+b)
    except:
        print("please enter numbers!")

if __name__ == "__main__":
    main()
