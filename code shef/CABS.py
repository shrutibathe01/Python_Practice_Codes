T = int(input())
tests = []
for i in range(T):
    tests.append([int(i) for i in input().split()])
for i in tests:
    if(i[0] < i[1]):
        print("FIRST")
    elif(i[0] > i[1]):
        print("SECOND")
    else:
        print("ANY")
        