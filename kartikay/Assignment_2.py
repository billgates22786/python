#Q1.WAP Ask user to input a number and then month name corresponding to that number
x=int(input("Enter the month number: "))
if(x==1):
    print("January")
elif(x==2):
    print("February")
elif(x==3):
    print("March")
elif(x==4):
    print("April")
elif(x==5):
    print("May")
elif(x==6):
    print("June")
elif(x==7):
    print("July")
elif(x==8):
    print("August")
elif(x==9):
    print("September")
elif(x==10):
    print("October")
elif(x==11):
    print("November")
elif(x==12):
    print("December")
else:
    print("Invalid Input")

#Q2 WAP Ask user to input 2 number,
#tell the followings
 #1. Both number are equal or not
 #2. Which is Bigger in both 
#3. Either First NUmber is smaller or equal to Second Number 
#4. Print your first name 5 times is first number is
# greather than second and print your surname 3 times if 1st no
# is less than second
print("*****************************************************************************************************************************")
name="Kartikay"
last="Jain"
y=int(input("Enter first number:"))
z=int(input("Enter Second number:"))
if(y==z):
    print("Both the numbers are equal")
elif(y>z):
    print(y,"is greater than",z)
    for i in range(5):
        print(name)
elif(y<z):
    print(y,"is less than",z)
    for i in range(2):
        print(last)
elif(y<z or y==z):
    print("Either First NUmber is smaller or equal to Second Number ")


#Q3  Using User input ask user to input 2 string and tell followings 
#1. using == tell both string equal or not
#2. using is operator tell both equal or not
print("*****************************************************************************************************************************")
string1 = input("Enter the first random string: ")
string2 = input("Enter the second random string: ")
if string1 == string2:
    print("Both strings are equal")
else:
    print("Strings are not equal")
if string1 is string2:
    print("Both strings are the same")
else:
    print("Strings are not the same")


#Q4 ask user to input 2 string and convert it into numbers and using is op tell both are euqal or not       
print("*****************************************************************************************************************************")
ab=input("Enter first string:")
ba=input("Enter second string:")
print("Id of first number:",id(ab))
print("Id of second number:",id(ba))
if(ab == ba):
    print("Both Strings are the same")
else:
    print("Both Strings are not equal")


#Q5 Create a menu drive program to peform the calculator as below
#Welcome to Sada Calculator
#Select your choice
#1. Addition
#2. Substration
#3. Division
#4. Multiplication
#5. Power
#6. Reminder
print("*****************************************************************************************************************************")
print("Welcome to Sada Calculator")
first=float(input("Enter First Number:"))
second=float(input("Enter Second Number:"))
print("\nSelect your choice:")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")
print("5. Power")
print("6. Remainder")
print("7. Exit")
choice = input("Enter your choice (1-7):")
if(choice=="1"):
    print("Add: ",first+second)
elif(choice=="2"):
    print("Sub: ",first-second)
elif(choice=="3"):
    if second == 0:
        print("Cannot divide by zero!")
    else:
        print("Division: ",first/second)
elif(choice=="4"):
    print("Multiplication: ",first*second)
elif(choice=="5"):
    print("Power: ",first**second)
elif(choice=="6"):
    print("Remainder: ",first%second)
elif(choice=="7"):
     print("Exit")
else:
    print("Invalid Input")


#Q7 Ask User to input a Number and with + or - and perform followings
#OP
 #  Enter a no: 567
  # Enter OP(+,-): +
   #0,1,2,3.......566
   #if -
   #  #567...>..... 1


number=int(input("Enter a number:"))
operation=input("Enter OP (+ or *):")
if (operation=="+"):
    for i in range(number):
        print(i)
elif(operation=="-"):
    for i in range(number,0,-1):
        print(i)
    else:
        print("INVALID OPERATION")


#Q8  #Question 7
  # Ask user to input a number and tell all even number upto that number
#Eg:
 #  input a num:29
 #  Even are:
 #  2,4,6,... 28

even = int(input("Enter the number: "))
if even % 2 == 0:
    print(f"Even numbers from 0 to",even,"are:")
    for i in range(0, even+1, 2):
        print(i)
else:
    print("The number is not even.")
