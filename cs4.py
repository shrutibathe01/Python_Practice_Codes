def Large_No(num1,num2,num3):
    if (num1>=num2) and (num1>=num3):
        print("Largest number is",num1)
    elif (num2>=num1) and (num2>=num3):
        print("Largest number is",num2)
    else:
        print("Largest number is",num3)

num1=float(input("First number:"))
num2=float(input("Second number:"))
num3=float(input("Third number:"))
Large_No(num1,num2,num3)
