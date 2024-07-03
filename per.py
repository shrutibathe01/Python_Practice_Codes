name=input("Enter the name: ")
if(name.isalpha()==False):
    print("Enter Valid Name")
    
rollNo=input("Enter Roll Number: ")
if(rollNo.isnumeric()==False):
    print("Enter Valid RollNumber")
M=[]
total=0    
print("Enter marks in order English,Hindi,Maths,Science and Social Science")
for i in range(5):
    marks=int(input("Enter the Marks: "))
    M.append(marks)
    total=total+marks
    if(not(marks>=1 and marks<=100)):
        print("Enter valid marks")
        break
    
percentage=0
percentage = ((total/500)*100)
print()
print("Roll No : ",rollNo)
print("Name : ",name)
print("English Marks: ",M[0])
print("Hindi Marks: ",M[1])
print("Maths Marks: ",M[2])
print("Science Marks: ",M[3])
print("Social Science Marks: ",M[4])
print("Percentage = %.2f"%percentage)
if(percentage>=36):
    print("Pass")
else:
    print("Fail")

    