import re
def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
            return 1
        else:
            return -1

result1=text_match("abc")
result2=text_match("a")
if (result1==1):
    print("Match Found")
else:
    print("Match not Found")
    
if (result2==1):
    print("Match Found")
else:
    print("Match not Found")