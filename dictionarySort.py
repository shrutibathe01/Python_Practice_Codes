def sort_dict(person):
    Asorted_person=sorted(person.items(),key=lambda x:x[1])
    resultA = dict(Asorted_person)
    print()
    print("Dictionary after Ascending sort: ",resultA)
    
    Dsorted_person=sorted(person.items(),key=lambda x:x[1],reverse=True)
    resultD = dict(Dsorted_person)
    print()
    print("Dictionary after Descending sort: ",resultD)
    
    
print("Enter the Total Number of Elements: ")
T=int(input())
person={}

for i in range(T):
    print(f"Enter the {i} person name: ",end='')
    name=input()
    print(f"Enter the {i} person age: ",end='')
    age=input()
    
    person[name]=age

print()    
print("Original dictionary: ",person)

resultA=sort_dict(person)



