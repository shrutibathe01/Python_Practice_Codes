"""No=int(input("Enter the number:"))
Rev=0
if(No<=0):
    print("Please entered positive number")
else:
    while(No!=0):
        digit=No%10
        #print(digit,end="")
        Rev=Rev*10 + digit
        No=No//10
print(Rev)"""

str=(input("Enter your number: "))

str1=str[::-1]
print(str1)

"""str="Shruti"
str2=str.reverse()
print(str2)"""