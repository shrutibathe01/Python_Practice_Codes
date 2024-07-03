def amstrong(num):
    tup=[int(x) for x in str(num)]
    m=len(tup)
    n=0
    for x in tup:
        n=n+x**m
    print("Sum is",n)
    if n==num:
        return 1
    else:
        return -1

num=int(input("Enter number: "))
result=amstrong(num)
if result==1:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
    
