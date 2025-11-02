#Q1.Write a program that prints the numbers from 1 to 50. 
# For multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". 
# For numbers which are multiples of both three and five, print "FizzBuzz".
for i in range(1, 51):  
    if i%3==0 and i%5==0: 
        print("FizzBuzz")
    elif i%3==0:  
        print("Fizz")
    elif i%5==0:  
        print("Buzz")
        

#Q2. Write a program to print all prime numbers between 1 and 100
print("Prime Numbers from 1 to 100:")
for i in range(1, 101):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)


# #Q3.
# Write a program that asks the user for a score between 0 and 100 and prints the corresponding grade. The grading scheme is:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F            
k = int(input("Enter your score between 0 and 100: "))
if k < 60:
    print("Grade: F")
elif 60 <= k <= 69:
    print("Grade: D")
elif 70 <= k <= 79:
    print("Grade: C")
elif 80 <= k <= 89:
    print("Grade: B")
elif 90 <= k <= 100:
    print("Grade: A")
else:
    print("Invalid score Please enter a score between 0 and 100.")
    
    
#Q4.
# Write a program that prints the multiplication table (from 1 to 10) for a given number
t=int(input("Enter a number:"))
print("Table of",t,":")
for i in range(11):
    print(t,"*",i,"=",t*i)
    
    
#Q5.
# Write a program to create a list of the squares of the even numbers from 1 to 20.    
for i in range(1,21):
    if i%2==0:
        print("Square of",i,"is:",i*i)


#Q6.
# Write a program to check if a given year is a leap year. 
# A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.
j=int(input("Enter the year:"))
if j%4==0:
    print("Leap Year")
else:
    print("Non Leap Year")    
    
    
#Q7.
# Write a program that takes the lengths of three sides of a triangle 
# as input and determines the type of triangle (equilateral, isosceles, or scalene).    
a=int(input("Enter the first side of length:"))
b=int(input("Enter the second side of length:"))
c=int(input("Enter the third side of length:"))
if a==b==c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")  
else:
    print("Scalene Triangle")  
    
    
#Q8.
# Write a program that takes an integer input from the user and classifies it as positive, negative, or zero.    
m=int(input("Enter a number"))
if m>0:
    print("It is a positive integer ")
elif m<0:
    print("It is a negative integer ")
elif m==0:
    print("Zero") 
  
  
# #Q9.
# Write a program that checks the strength of a password based on the following criteria:
# At least 8 characters long
# Contains both uppercase and lowercase characters
# Contains at least one digit
# Contains at least one special character (e.g., !, @, #, $, etc.)  
password=input("Enter Your Password:")
if len(password)<8:
    print("Weak Password: Less than 8 characters")
    

#Q10.
# Write a program that calculates the Body Mass Index (BMI) and categorizes it based on the following criteria:
# BMI < 18.5: Underweight
# 18.5 <= BMI < 24.9: Normal weight
# 25 <= BMI < 29.9: Overweight
# BMI >= 30: Obesity
weight=float(input("Enter Your Weight in KG:"))
height=float(input("Enter Your Height in meter square:"))
BMI=weight*height*height
if BMI<18.5:
    print("UnderWeight")
elif 18.5<=BMI<24.9:
    print("Normal Weight")
elif 25<=BMI<29.9:
    print("OverWeight")
elif BMI>=30:
    print("Obesity")


#Q11.Write a program that takes an integer input representing a day of the week 
# (1 for Monday, 2 for Tuesday, etc.) and prints the corresponding day name.            
x=int(input("Enter the day number: "))
if(x==1):
    print("Monday")
elif(x==2):
    print("Tuesday")
elif(x==3):
    print("Wednesday")
elif(x==4):
    print("Thursday")
elif(x==5):
    print("Friday")
elif(x==6):
    print("Saturday")
elif(x==7):
    print("Sunday")
else:
    print("Invalid Option")
                                

#Q12.
# Write a program that calculates the discount on a product based on the following criteria:
# If the price is greater than $1000, a discount of 10% is applied.
# If the price is between $500 and $1000, a discount of 5% is applied.
# If the price is below $500, no discount is applied.                                
# Get the amount from the user
amount = float(input("Enter the amount: "))
if amount>1000:
    discount=amount*0.10
elif amount>=500:
    discount=amount*0.05
else:
    discount=0
    
price = amount - discount

# Print the results
print("Original Amount",amount)
print("Discount",discount)
print("Final price",price)


#Q13. Write a program to find the sum of the first n natural numbers.
numb=int(input("Enter the natural num: "))
n=0
for i in range(numb+1):
    n+=i

print("sum of all natural numbers:",n)


#Q14.
# Write a program to calculate the factorial of a given number
f = int(input("Enter the number of which you want to find factorial: "))
tf = 1 
for i in range(1, f + 1):
    tf *= i  
print("The factorial of", f, "is:", tf)


#Q15.
# Write a program to count the number of vowels in a given string
kat = input("Enter a random string: ").lower() 
vowels = "aeiou"
count = 0
for j in kat:
    if j in vowels:
        count += 1
print("Number of vowels:", count)


#Q16.
# Write a program to find the sum of the digits of a given number.
input = int(input("Enter a number: "))
totalss = 0
for digit in str(input):
    totalss += int(digit)  
print(f"The sum of the digits is: {totalss}")


#Q17.
# Write a program to print a pattern of stars. For example, if n = 5, the pattern should be
# *
# **
# ***
# ****
# *****
stars=int(input("The amount of stars: "))
for i in range(1, stars+ 1):
    for j in range(i):
        print("*", end="")
    print()  


#Q18.
# Write a program for a number guessing game where the computer randomly selects a number between 1 and 100, and the user tries to guess it. 
# The program should give hints if the guess is too high or too low.
import random as rn
computer_guess = rn.randint(1, 100)
attempts = 5 
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. You have 5 attempts to guess it.")
for attempt in range(1, attempts + 1):
    guess = int(input("Attempts",attempt,": Enter your guess: "))
    if guess < computer_guess:
        print("Too low Try again.")
    elif guess > computer_guess:
        print("Too high Try again.")
    else:
        print("Congratulations! You've guessed the number",computer_guess,"correctly in",attempt,"attempts.")
        break  
else:
    print("Sorry You have used all your attempts. The correct number was",computer_guess)
   
