f=open("Students.csv","w")
f.write('name,rollNo,age\n')
f.write('Kartikay,1,19\n')
f.write('Suresh,2,26\n')
f.write('Nikhil,3,23\n')
f.close()
f=open("Students.csv","r")
for line in f:
  print(line.strip(','))
f.close()
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="StudentInfo")
mycursor=mydb.cursor()
with open('Students.csv',"r") as f:
    for row in f:
        name = 'name'
        rollNo = 'rollNo'
        age = 'age'
        mycursor.execute("INSERT INTO Students (name,rollNo,age) VALUES (%s,%s,%s)",(name,rollNo,age))
        mycursor.commit()
        mycursor.close()
        
