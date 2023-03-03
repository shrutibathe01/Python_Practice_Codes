# cook your dish here
T = int(input())
tests = []
for i in range(T):
    tests.append([int(i) for i in input().split()])
for i in tests:
    if((i[0]*i[1] < 0) or (i[0]*i[2] < 0) or (i[1]*i[2] < 0)):
        print("YES")
    else:
        print("NO")