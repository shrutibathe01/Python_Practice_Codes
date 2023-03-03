"""iNo=int(input("Enter the number:"))
iNum=iNo
iRev=0
if(iNo<=0):
    print("Please entered positive number")
else:
    while(iNo>0):
        iDigit=iNo%10
        #print(iDigit)
        iRev=iRev*10 + iDigit
        iNo=iNo//10
if(iNum==iRev):
        print("Number is Palindrome")
else:
        print("Number is not Palindrome")"""
        

string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")

