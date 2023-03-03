# We have populated the solutions for the 10 easiest problems for your support.
# Click on the SUBMIT button to make a submission to this problem.

T = int(input())
tests = []
for i in range(T):
    tests.append([int(i) for i in input().split()])
for i in tests:
    print(i[0]%i[1])
