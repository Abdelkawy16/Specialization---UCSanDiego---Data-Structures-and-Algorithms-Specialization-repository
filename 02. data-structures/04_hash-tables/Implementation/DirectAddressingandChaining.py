from datetime import datetime, timedelta

def main():
    print("HIIIIIIII")

#Direct addressing (fast but it used a lot of memory)
""" def UpdateAccessList(log, i, j, A):
    while log[i].time <= datetime.now():
        A[Int(log[i].IP)] += 1
        i += 1
    while log[j].time <= datetime.now() - timedelta(hours = 1):
        A[Int(log[j].IP)] -= 1
        j += 1

def Int(IP):
    IP = IP.split(":")
    x = IP[0] * 2 ** 24 +IP[1] * 2 ** 16 + IP[2] * 2 ** 8 + IP[3] * 2
    return x

def AccessedLastHour(IP):
    return A[Int(IP)] > 0 """

#Direct addressing (List based mapping)
def UpdateAccessList(log, i, A):
    while log[i].time <= datetime.now():
        A.append(log[i])
        i += 1
    while A[0].time <= datetime.now() - timedelta(hours = 1):
        A.pop(0)

def AccessedLastHour(IP, A):
    for i in range(len(A)):
        if A[i].IP == IP:
            return True
    return False 

def AccessedCountLastHour(IP, A):
    count = 0
    for i in range(len(A)):
        if A[i].IP == IP:
            count += 1 
    return count


if __name__ == '__main__':
    main()
    