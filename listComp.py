def set1(list1,list2):
    a = set(list1)
    b = set(list2)

    if a==b:
        print("Yes")
    else:
        print("No")
        

list1=[]
list2=[]
n = 5

for i in range(0,n):
    print("Enter the elements of list1: ")
    element=int(input())
    list1.append(element)

for i in range(0,n):
    print("Enter the elements of list2: ")
    element=int(input())
    list2.append(element)

print(list1)
print(list2)

list1.sort()
list2.sort()
if(list1==list2):
    print("Yes")
else:
    print("No")
    
set1(list1,list2)


    

