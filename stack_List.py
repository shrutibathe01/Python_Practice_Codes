No=int(input("Enter the number of elements:"))
my_list=[]

while (No > 0):
    x=input("Enter elements: ")
    my_list.append(x)
    No=No-1
print(my_list)
    
print("Popped elements are: ")
while (len(my_list)):
    print(my_list.pop())
    
    
    
    

    

