def check_No(l,u,n):
    if n in range(l,u):
        print(n,"is in the given range")
    else:
        print(n,"is not in the given range")


lower=int(input("Lower bound: "))
upper=int(input("Upper bound: "))
No=int(input("Number to search: "))

check_No(lower,upper,No)

