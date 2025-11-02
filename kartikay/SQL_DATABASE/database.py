import mysql.connector

try:
    connection = mysql.connector.connect(
            host="localhost",
            port=4306,
            user="root",
            password="",
            database="kartikay"
        )
    print("Connection successful")
except:
    print("Connection Unsuccessful")
    
cursor=connection.cursor()
def register(data):
    try:
   
        cursor.execute("insert into user (name,email,password) values (%s,%s,%s)",data)
        connection.commit()
        return True
    except:
        print("error")
        
def login(data):
        try:
            cursor.execute("select * from user where email=%s and password=%s",data)
            return cursor.fetchall()
            #return cursor.fetchone()
        except:
            print("error")
            
def view():
    try:
        cursor.execute("select * from user")
        return cursor.fetchall()
    except:
        print("error")
        
def update(data):
    try:
        cursor.execute("update user set name=%s,email=%s,password=%s where id=%s",data)
        connection.commit()
        return True
    except:
        print("error")
        
def getone(data):
    try:
        cursor.execute("select * from user where id=%s",data)
        return cursor.fetchone()
    except:
        print("error")
    
def delete(data):
    try:
        cursor.execute("delete from user where id=%s",data)
        connection.commit()
        return True
    except:
        print("error")