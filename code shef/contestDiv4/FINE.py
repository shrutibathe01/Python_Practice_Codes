# cook your dish here
T = int(input())
for i in range(T):
    num = int(input())
    if(num <= 70):
        print("0")
    elif((num > 70) and (num <= 100)):
        print("500")
    else:
        print("2000")