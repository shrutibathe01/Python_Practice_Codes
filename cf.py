def fahrenheit(Celsius):
    Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
    return list(Fahrenheit)
    
print("Enter Number of total celsius: ")
No=int(input())
Celsius=[]
for i in range(No):
    print(f"Enter the {i} Celsius : ",end='')
    C=float(input())
    Celsius.append(C)

result=fahrenheit(Celsius)
print(result)
    

