T = int(input())
lst1 = []
lst2 = []
for i in range(T):

    n = int(input("Enter number of elements : "))
    lst1 = [int(n) for n in input().split()]
    lst2 = [int(n) for n in input().split()]
    print(lst1)
    op = int(input())
    while (op != 0):
        i = int(input())
        j = int(input())
        x = lst1[i-1]
        lst1[i-1] = lst2[j-1]
        lst2[j-1] = x
        op = op-1 
        print(lst1)
    lst1.sort()
    l = lst1[-1]-lst1[0]
    print(l)   
               