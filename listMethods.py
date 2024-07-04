def extend_list(list1):
    T2=int(input("Enter the total number of elements that you want to append: "))
    list2=[]
    for i in range(T2):
        print(f"Enter {i} element of list",end='')
        ele=input()
        list2.append(ele)
    print("Original list2 is: ",list2)
    list1.extend(list2)
    print("List1 after Extended is: ",list1)
    
def sort_list(list1):
    list1.sort()
    print("Sorted list is: ",list1)
    print()

def reverse_list(list1):
    list1.reverse()
    print("Reverse list is: ",list1)
    print()
    
def pop_listElement(list1):
    print("Enter the position that you want to pop: ")
    pos=int(input())
    if pos in range(len(list1)):
        list1.pop(pos)
        print(list1)
    else:
        print("Invalid Position")
    



print("Select the option of list methods")
print()
print("Enter 1 to Extend the list")
print("Enter 2 to sort the list")
print("Enter 3 to Reverse the list")
print("Enter 4 to pop the element of list")
print("Select the option of list methods")
option=int(input())
T=int(input("Enter the total number of elements: "))
list1=[]
for i in range(T):
    print(f"Enter {i} element of list : ",end='')
    ele=input()
    list1.append(ele)
print("Original list1 is: ",list1)
print()

if(option==1):
    extend_list(list1)
elif(option==2):
    sort_list(list1)
elif(option==3):
    reverse_list(list1)
elif(option==4):
    pop_listElement(list1)
else:
    print("Invalid Option")

    
    