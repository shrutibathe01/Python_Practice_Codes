class exception(Exception):
    pass
try:  
    a = 10/0
    print (a)
except ArithmeticError:  
    print ("This statement is raising an arithmetic exception.")
try:
    array = [ 0, 1, 2 ]
    print (array[3])
except IndexError:
    print("This is raising index error")
else:  
    print ("Success.")
try:
    from feh7 import exception
except:
    print("Module not available")