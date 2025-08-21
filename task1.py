# Even OR Odd
num=int(input("Enter a number: "))
if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")
    

# Positive,Negative or Zero
num1=int(input("Enter a number: "))
if num1>0:
    print("Positive Number ")
elif num1<0:
    print("Negative Number")
else:
    print("Zero Number")
    

# Greatest of two numbers
num3=int(input("Enter a first number: "))
num4=int(input("Enter a second number: "))
if num3>num4:
    print(f"{num3} is greater than {num4}")
else:
    print(f"{num4} is greater than {num3}")

# Pass Or Fail
marks=int(input("Enter a number: "))
if marks>=40:
    print("Pass")
else:
    print("Fail")
    