f=open("intro.txt","a")
f.write("""Hello, My Name is Shruti Satish Bathe. I am from Pune. 
        Currently Pursuing Last year of Master in Industrial Mathematics with Computer Application""")
f.close
f = open("intro.txt", "r")
print(f.read())
