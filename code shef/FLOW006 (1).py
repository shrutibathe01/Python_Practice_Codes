# We have populated the solutions for the 10 easiest problems for your support.
# Click on the SUBMIT button to make a submission to this problem.

a = int(input(''))
for i in range(a):
  b = int(input(''))
  c = 0
  d = 0
  while b != 0:
    c = b % 10
    d = d + c
    b = b // 10
  print(d)


