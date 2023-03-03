#create table student and insert record into it
from os import error
import mysql.connector as sql

def connection():
    try:
        m=sql.connect(host="localhost",user="root",password="",database="practical")
        return m
    except error:
        print(error)    
        
def createtable():
    con=connection()
    cursor=con.cursor()
    query="create table student1 (stu_no int(10) primary key, stu_name varchar(50), stu_marks varchar(50))"
    cursor.execute(query)
    con.commit()
    print("Table created successfully!!!")

def insertData(student):
    con=connection()
    cursor=con.cursor()
    query="Insert into student1 values('{}','{}','{}')".format(student[0],student[1],student[2])
    cursor.execute(query)
    con.commit()
    print("Data inserted successfully!!!")

def displayData():
    con=connection()
    cursor=con.cursor()
    query="select * from student1"
    cursor.execute(query)
    result=tuple(cursor.fetchall())
    
    print("S.No\tStudent name\tMarks")
    for x in result:
        print(x[0],"\t",x[1],"\t\t",x[2])

con=connection()
cursor=con.cursor()
#query="Create Table Student(Student_no int(10) primary key,Student_Name varchar(50),Marks int(20))"
#cursor.execute(query)   

no=int(input("Enter student no: "))
name=input("Enter student name: ")
marks=float(input("Enter student Marks: "))

createtable()
student1=[no,name,marks]
insertData(student1)
displayData()

if con:
    con.close()
    print("sql connection closed")