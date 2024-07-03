def fact(num):
    if num<0:
        print("Factorial does not exist")
    else:
        b=1
        for a in range(1,num+1):
            b=b*a
        return b
        
num=int(input("Enter number here: "))
result=fact(num)
print("Factorial of",num,"is",result)
