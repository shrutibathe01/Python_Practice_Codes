T = int(input())
tests = []
for i in range(T):
    tests.append([int(i) for i in input().split()])
for i in tests:
    if(i[0] < i[1]):
        print(i[1] - i[0])
    else:
        print(i[0] - i[1])