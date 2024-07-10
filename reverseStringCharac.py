#Reverse String character

str1=input("Enter String: ")
i=len(str1)-1
while i>=0:
    print(str1[i],end='') 
    i=i-1
    
"""OR
output=''
i=len(str1)-1
while i>=0:
    output=output+str1[i]
    
    i=i-1
print(output)
"""
print("")

#Reverse by slicing
print("Reverse by slicing")
output=str1[::-1]
print(output)
print(type(output))

print("")

#Reverse by reversed function
print("Reversed by reversed function")
r=reversed(str1)
for ch in r:
    print(ch,end='')
"""OR
output=''.join(r)
print(output)"""