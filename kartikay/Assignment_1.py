#Q1. WAP in which print the following
       #Your Name
       #Your age
       #Your college as below format
#"Hello, my name is Gaurav I am 31 years old and attend IHGI College"
name="Kartikay Jain"
age=18
college="Innocent Hearts Group Of Institutions"
print("Hello, My name is",name,"I am",age,"years old and attend",college,)


#Q2. Take Different 5 Variable with different data types and print variables values along with types
print("**************************************************************************************************")
integer=8055
floating=99.11
string="Snitch"
boolean=120
ragnarok=585
print(integer,type(integer))
print(floating,type(floating))
print(string,type(string))
print(boolean,type(boolean))
print(ragnarok,type(ragnarok))


#Q3. Ask User to input Your Name and age and print the following
#My Name is Gaurav having age is 31 and i have 69 year left to become 100 year old
print("**************************************************************************************************")
name=input("Enter your name:")
age=int(input("Enter your age:"))
lifetime=100-age
print("My Name is",name,"having age",age,"and I have",lifetime,"year left to become 100 year old")


#Q4 Ask user to input 2 numbers and print
#1. Sum
#2. Sub
#3. Multiplication
#4. 1st number/second Number
print("**************************************************************************************************")
x=int(input("ENTER FIRST NUMBER:"))
y=int(input("ENTER THE SECOND NUMBER:"))
print("ADDITION OF THE TWO NUMBERS:",x+y)
print("SUBTRACTION OF THE TWO NUMBERS:",x-y)
print("MULTIPLICATION OF THE TWO NUMBERS:",x*y)
print("DIVISION OF THE TWO NUMBERS",x/y)


#Q5. Ask user to input a value and convert that value in variable data types like int,float,str,bool,and at last to int again
print("**************************************************************************************************")
print("input the value below for conversion")
z=input("Enter the value:")
print(int(z))
print(float(z))
print(bool(z))
print(str(z))
print(int(z))


#Q6. Ask user to input 2 numbers and tell the following
#1. Sum
#2. Substration
#3. Multiplication
#4. Division
#5. Modulus
#6. Also multiply your name a times
#7. Show a**b result
print("**************************************************************************************************")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("Addition of the two numbers is:",a+b)
print("Subtracton of the two numbers is:",a-b)
print("Multiplication of the two numbera is:",a*b)
print("Division of two numbers is:",a/b)
print("Modulus of two numbers is",a%b)
print("Multiply of name with first number:","kartikay"*a)
print("Square of the number is:",a**b)











