import re
def validateP(p):
    x = True
    while x:  
        if (len(p)<9):
            print("Password should contain Atleast 9 digit/character")
            break
        elif not re.search("[a-z]",p):
            print("Password should contain 1 Small character")
            break
        elif not re.search("[0-9]",p):
            print("Password should contain digit from 0-9")
            break
        elif not re.search("[A-Z]",p):
            print("Password should contain 1 Capital character")
            break
        elif not re.search("[$_%]",p):
            print("Password should contain one of ($,_,%) character")
            break
        elif re.search("\s",p):
            break
        else:
            print("Valid Password")
            x=False
            break

    if x:
        print("Not a Valid Password")
    
password=input("Enter your password: ")
validateP(password)
    
