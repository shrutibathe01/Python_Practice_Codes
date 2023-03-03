n=int(input("Enter number: "))

for i in range(n+1):
  for j in range(i):
    print("*",end='')
  space=2*n-2*i
  for k in range(space):
   print(" ",end='')
  for m in range(i):
    print("*",end='')
  print()