my_int = int(input("Enter the number: "))

my_list = [int(x) for x in str(my_int)]

n=len(my_list)

a=0
for x in my_list:
    a=a+x**n      
print(a)

if my_int==a:
    print("{} is amstrong".format(my_int))
else:
    print("{} is not a amstrong".format(my_int))