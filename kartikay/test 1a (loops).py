#Loops
#Q1. Write a script that counts the number of vowels (a, e, i, o, u) in a given string s using a while loop and prints the count. 
# k=input("Enter a random string: ")
# print("Vowels: a,e,i,o,u")
# count=0
# for j in k:
#     if j=="a" or j=="A" or j=="e" or j=="E" or j=="i" or j=="I" or j=="o" or j=="O" or j=="u" or j=="U":
#         count+=1

# print("Total number of vowels in the above string:",count) 

# #Q2. Write a script that calculates and prints the sum of all multiples of 3 or 5 below a given limit, where limit is provided by the user.
# z=int(input("Enter Range:"))
# print("The number which are the multiples of 3 and 5 are:")
# for i in range(z):
#     if i%3==0 or i%5==0:
#         print(i)
        

#Q3. Write a script that generates and prints the first n numbers in the Fibonacci sequence using a for loop, where n is a positive integer given by the user.        
a=0 
b=1 
for i in range(2,10):
    c=a+b
    print(c)
    a=b
    b=c 
    