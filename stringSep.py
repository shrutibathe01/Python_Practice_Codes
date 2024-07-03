str="ASdfesD@#HBDHB&^GUV%^*H45fdvnhw74w5e54uuU"
lower=[]
upper=[]
number=[]
special=[]

for x in range(len(str)):
    if (str[x]>='A' and str[x]<='Z'):
        upper.append(str[x])
    elif (str[x]>='a' and str[x]<='z'):
        lower.append(str[x])
    elif (str[x]>='0' and str[x]<='9'):
        number.append(str[x])
    else:
        special.append(str[x])

stringU=''        
for elements in upper:
    stringU=stringU+elements
print("Upper Charactes:",stringU)

stringL=''
for elements in lower:
    stringL=stringL+elements
print("Lower Charactes:",stringL)

stringN=''
for elements in number:
    stringN=stringN+elements
print("Numbers :",stringN)

stringS=''
for elements in special:
    stringS=stringS+elements
print("Special Charactes:",stringS)
