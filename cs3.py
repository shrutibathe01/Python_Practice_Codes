def check_year(year):
    if year%400==0 and year%100==0:
        print("Leap year")
    elif year%4==0 and year%100 != 0:
        print("Leap year")
    else:
        print("Not a leap year")
    

year=int(input("Enter year: "))
check_year(year)
