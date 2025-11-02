import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="userin"
)
mycursor=mydb.cursor()
n=int(input("Enter number of data to be stored: "))
for i in range(n):
    a=int(input("Enter a roll number: "))
    
    sql="SELECT * FROM information WHERE rollno=%s"
    val=(a,)
    mycursor.execute(sql, val)
    myresult=mycursor.fetchall()

    if myresult: 
        print("Already exists")
        print("Deleted")
        sql="UPDATE FROM information WHERE rollno=%s"
        b=input("Enter updated name:")
        c=int(input("Enter updated age:"))
        val=(a,)
        mycursor.execute(sql, val)
        mydb.commit()
    else:
        b=input("Enter a name: ")
        c=int(input("Enter age: "))
        sql="INSERT INTO information (rollno, name, age) VALUES (%s, %s, %s)"
        val=(a, b, c)
        mycursor.execute(sql, val)
        mydb.commit()
        print("RECORD INSERTED")
    mycursor.execute("SELECT * FROM information")
    result=mycursor.fetchall()
    for x in result:
        print(x)
