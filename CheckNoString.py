import re
def checkNoEnd(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return 1
    else:
        return -1

result1=checkNoEnd("gmail123")
result2=checkNoEnd("123gmail")
if (result1==1):
    print("Match Found")
else:
    print("Match not Found")
    
if (result2==1):
    print("Match Found")
else:
    print("Match not Found")