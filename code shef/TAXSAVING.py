# cook your dish here
T = int(input())
for _ in range(T):
    x,y = map(int , input().split())
    if(x > y):
        c=x-y
        print(c)
    else:
        print(y)
    