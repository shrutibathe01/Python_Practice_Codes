def fibonacci(value):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,value):
        c=a+b
        a=b
        b=c
        print(c)
        
No=int(input("Enter the number: "))
fibonacci(No)