def fact(No):    
    factorial = 1    
    if No < 0:    
        print(" Factorial does not exist for negative numbers")    
    elif No == 0:    
        print("The factorial of 0 is 1")    
    else:    
        for i in range(1,No + 1):    
            factorial = factorial*i    
        print("The factorial of",No,"is",factorial)   