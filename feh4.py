try:
    f1 = open("intro.txt")
    print("File exist")
    f1.close()
    f2 = open("demo.txt")
    print("File exist")
    f2.close()

except IOError:
    print("File not found.")