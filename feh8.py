while(True):
    ans = input("Enter a input : ")

    if ans[0]=="-":
        r = ans[1:].isdigit()
        if r==True:
           print("Right")
           break
    elif ans.isdigit():
        print("Right")
        break
    else:
        print("\nEnter valid digit .\n")
