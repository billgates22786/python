#Q1 Write a script that checks if a given integer n is a prime number and prints "Prime" 
# if it is, and "Not Prime" if it isn't. Given a list of integers nums  
# print("Prime Numbers from 1 to 100:")
for i in range(1, 101):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)

a=int(input("Enter a number: "))
if a<=1:
    print("Nah Prime nah Composite")
elif a==2:
    print("Prime Number")
else:
    f=False
    for i in range(2,int(a/2)+1):
        if (a % i)==0:
            f=True
            break
    if f==True:
        print("It is a Composite Number")
    else:
        print("It is a Prime Number")


#Q2. Write a script that categorizes each number as "positive", "negative", or "zero" and prints these categories with their respective lists.
b=int(input("Enter a number"))
if b>0:
    print("It is a positive integer ")
elif b<0:
    print("It is a negative integer ")
elif b==0:
    print("Zero") 
           