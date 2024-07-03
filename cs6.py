def range_No(l,u):
    for x in range(l,u+1):
        if x>1:
            for i in range(2,x):
                if x%i==0:
                    break
            else:
                print(x, end=" ")

range1=int(input("Enter start digit of interval: "))
range2=int(input("Enter last digit of interval: "))
range_No(range1,range2)

