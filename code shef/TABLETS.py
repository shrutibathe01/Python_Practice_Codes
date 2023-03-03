# cook your dish here
T = int(input())
tests = []
for i in range(T):
    tests.append([int(i) for i in input().split()])
for i in tests:
    x = i[0]*3
    if(x > i[1]):
        print("NO")
    else:
        print("YES")