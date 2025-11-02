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

cursor = connection.cursor()

def register(data):
    try:
        cursor.execute("INSERT INTO user (name, email, password) VALUES (%s, %s, %s)", data)
        connection.commit()
        return True
    except:
        print("Error")
        return False

def login(data):
    try:
        cursor.execute("SELECT * FROM user WHERE email=%s AND password=%s", data)
        return cursor.fetchall()
    except:
        print("Error")
        return None
