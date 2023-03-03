# cook your dish here
T = int(input())
tests = []
for i in range(T):
    tests.append([int(i) for i in input().split()])
for i in tests:
    if(i[0]*100 < i[1]*10):
        print("Disposable")
    elif(i[0]*100 > i[1]*10):
        print("Cloth")
    else:
        print("Cloth")