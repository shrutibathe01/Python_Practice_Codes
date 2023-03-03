No=int(input("Enter the number you want to check: "))
if((No%400==0) and (No%100==0)):  #century   2000
    #print("{} is a leap year".format(No))
    print(No,"is a leap year")
elif((No%4==0) and (No%100!=0)):  # non century
    print("{} is a leap year".format(No))
else:
    print("{} is not a leap year".format(No))