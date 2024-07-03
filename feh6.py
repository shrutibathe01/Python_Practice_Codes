def sq():
    while True:
        try:
            num = int(input("Enter a number: "))
        except:
            print("Enter a proper number")
            continue
        else:
            print("The square of the entered number is :", num**2)
            break
sq()