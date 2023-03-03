class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
""" def info(self):
    print("Entered name is:" + self.name)
    print("Entered name is:" + self.age)"""

nav=input("Enter the name:")
vay=input("Enter the age:")

obj = Person(nav,vay)
#obj.info()

print("Your name is" ,nav + " and age is" ,vay)
#print("Your age is" ,age)

