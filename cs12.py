def sum_N(num):
    if num<=0:
        print("Enter positive number")
    else:
        sum=0
        for x in range(1,num+1):
            sum=sum+x
        return sum
        
num=int(input("Enter number here: "))
result=sum_N(num)
print("Sum of first",num,"natural numbers is",result)