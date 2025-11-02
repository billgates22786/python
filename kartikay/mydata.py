import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="college")
mycursor=mydb.cursor()
a=int(input("ENTER THE ROLL NUMBER:"))
sql="SELECT * FROM info WHERE rollno=%s"
val=(a,)
mycursor.execute(sql,val)
myresult=mycursor.fetchall()
b=bool(myresult)
if b==True:
    for x in myresult:
        print(x)
    mydb.close()
    print("MySQL connection closed.")
else:
    print("NOT FOUND")
    mydb.close()
    print("MySQL connection closed.")
    
