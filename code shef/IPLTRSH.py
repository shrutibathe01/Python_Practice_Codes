# cook your dish here
T = int(input())
for _ in range(T):
    n,m = map(int, input().split())
    if(n > m):
        ans=n-m
        print(ans)
    elif(n<=m):
        print("0")