import re
str1 = '''The re package provides several methods to actually perform queries on an input string'''
#findall
r = re.findall(r"\S+[0-9]\S+", str1)
r1 = re.findall(r"^\w+",str1)
print(r1)
print(r)
#split
print((re.split(r'\s(?=[A-Z])',str1)))
#search
print(re.search(r"[A-Z]", str1))
#sub
print(re.sub("\s","_",str1))