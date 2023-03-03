rows = int(input("Enter number of rows: "))   # 5
for i in range(rows):                         # 1 to 5     
    for j in range(i+1): #4                     # i          1   1          
        print("* ", end="")                                 #2   1,2         
    print("\n")                                             #3   1            