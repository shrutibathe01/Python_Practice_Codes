import re
#shruti_123@gmail.com
condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
email=input("Enter Your Email:")
if re.search(condition,email):
    print("Valid Email")
else:
    print("Invalid Email")



"""import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def check(email):
	if(re.fullmatch(regex, email)):
		print("Valid Email")

	else:
		print("Invalid Email")

email = input("Enter email:")
check(email)"""