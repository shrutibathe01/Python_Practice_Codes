# cook your dish here
T = int(input())
tests = []
for i in range(T):
    tests.append([int(i) for i in input().split()])
for i in tests:
    if(i[0] + i[1] + i[2] == 180):
        print("YES")
    else:
        print("NO")