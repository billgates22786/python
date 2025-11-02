import csv
import mysql.connector


with open('Students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'rollNo', 'age'])
    writer.writerow(['Kartikay', 1, 19])
    writer.writerow(['Suresh', 2, 26])
    writer.writerow(['Nikhil', 3, 23])


with open('Students.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="StudentInfo"
)


mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Students (name VARCHAR(50), rollNo INT, age INT)")


with open('Students.csv', 'r') as f:
    next(f)
    for row in f:
        data=row.strip().split(',')
        name=data[0]
        rollNo=int(data[1])
        age=int(data[2])
        sql="INSERT INTO Students (name, rollNo, age) VALUES (%s, %s, %s)"
        val=(name, rollNo, age)
        mycursor.execute(sql, val)
        mydb.commit()


mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)


mycursor.execute("SELECT * FROM Students")
myresult=mycursor.fetchall()
for i in myresult:
    print(i)


mycursor.close()
mydb.close()

