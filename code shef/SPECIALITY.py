# cook your dish here
T = int(input())
tests = []
for i in range(T):
    tests.append([int(i) for i in input().split()])
for i in tests:
    if(i[0] != i[1] != i[2]):
        if((i[0]>i[1]) and (i[0]>i[2])):
            print("Setter")
        elif((i[1]>i[0]) and (i[1]>i[2])):
            print("Tester")
        else:
            print("Editorialist")