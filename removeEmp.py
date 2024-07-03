list1=["Mike","","Kelly","","Brad"]
for i in list1:
    if(i==""):
        x=list1.remove(i)
print("Final List After removing empty element: ",list1)