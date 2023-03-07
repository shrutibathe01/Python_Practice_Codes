import mariadb
mydb=mariadb.connect(host="localhost", user="root", password="", database="internship_task")
mycursor=mydb.cursor()
#create_table_query="create table students (First_name VARCHAR(255),Last_name VARCHAR(255),City VARCHAR(255),Percentage FLOAT)"
#mycursor.execute(create_table_query)
insert_query="""insert into students (First_name,Last_name,City,Percentage)
values("Shruti","Bathe","Pune",90),
("Amruta","Kulkarni","Mumbai",85),
("Rani","Tikale","Kolhapur",80),
("Asmita","Pimpalkar","Pune",80),
("Rohan","Dikhale","Nashik",95),
("Krishna","Chaudhari","Mumbai",90),
("Arvind","Ujjainkar","Aurangabad",85),
("Ashwini","Gopale","Khed",90);"""
mycursor.execute(insert_query)
select_query="select * from students"
mycursor.execute(select_query)
data=tuple(mycursor.fetchall())
for i in data:
    print(i)

print()
print()
query="select First_name,Last_name from students"
mycursor.execute(query)
result=mycursor.fetchall()
for i in result:
    print(i)
    
print()
print()
query2="select * from students where city='Pune'"
mycursor.execute(query2)
result=mycursor.fetchall()
for i in result:
    print(i)
    
print()
print()
query3="select * from students where Percentage>=85"
mycursor.execute(query3)
result=mycursor.fetchall()
for i in result:
    print(i)
    