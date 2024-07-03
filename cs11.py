num1=int(input("Lower Interval: "))
num2=int(input("Upper Interval: "))
for num in range(num1,num2+1):
    tup=[int(x) for x in str(num)]
    m=len(tup)
    n=0
    for x in tup:
        n=n+x**m
    if num == n:
        print(n,end=", ")