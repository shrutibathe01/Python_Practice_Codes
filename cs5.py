def check_prime(num):
    if num==1:
        print(num,"is not prime number")
    elif num>1:
        for i in range(2,num):
            if num%i==0:
                print(num,"is not prime number")
                break
        else:
            print(num,"is prime number")
    else:
        print(num,"is not prime")
    
num=int(input("Enter number here: "))
check_prime(num)

