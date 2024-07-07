import os

cities=[]

path = os.path.join("d:/HopeFoundation/Python/", "cities")
os.mkdir(path)

while True:
    choice=int(input("Do you want to enter city name \n if Yes press 1 else press 0:"))
    if(choice==0):
        break
    else:    
        c=input("Enter city name: ")
        name="d:/HopeFoundation/Python/cities/"+c[0]+".txt"
        f = open(name, "a")
        f.write(c)
        cities.append(c)