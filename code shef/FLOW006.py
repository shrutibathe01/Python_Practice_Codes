# We have populated the solutions for the 10 easiest problems for your support.
# Click on the SUBMIT button to make a submission to this problem.

T =int(raw_input())
for _ in range(T):
    result = 0
    num = str(raw_input())
    for word in num:
        result = result + int(word)
    print(result)    
        


