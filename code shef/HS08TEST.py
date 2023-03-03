# We have populated the solutions for the 10 easiest problems for your support.
# Click on the SUBMIT button to make a submission to this problem.

x, y = map(float, raw_input().split())
if x%5==0 and y-.5>=x:
    print(format(y-x-0.50,".2f"))
else:
    print(format(y,".2f"))
