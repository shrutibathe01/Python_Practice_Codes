# cook your dish here
import math
T = int(input())
tests = []
for i in range(T):
    tests.append([float(i) for i in input().split()])
for i in tests:
    alice = math.sqrt((i[0]**2) + (i[1]**2))
    bob = math.sqrt((i[2]**2) + (i[3]**2))
    if(alice > bob):
        print("ALEX")
    elif(alice < bob):
        print("BOB")
    else:
        print("EQUAL")