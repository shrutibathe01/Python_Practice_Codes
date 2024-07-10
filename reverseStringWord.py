str1="Hello I am Shruti"
s=str1.split()
i=len(s)-1
while i>=0:
    print(s[i],end=' ')
    i=i-1

print("")

#Reverse by slicing
print("Reverse using slicing")
slice=s[::-1]
output=" ".join(slice)
print(output)

print("")

#Reverse by Reversed
print("Reverse by reversed")
r=reversed(s)
output=" ".join(r)
print(output)