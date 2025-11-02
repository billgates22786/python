# def partition():
#     print(" ")
#     print("********************************************************************************************************************************************************************************************")
#     print(" ")
# #Q1. Find prime number using user defined function.
# def prime_number(a):
#     if a<=1:
#         print("Nah Prime nah Composite")
#     elif a==2:
#         print("Prime Number")
#     else:
#         f=False
    # for i in range(2,int(a/2)+1):
    #     if (a % i)==0:
#             f=True
#             break
#     if f==True:
#         print("It is a Composite Number")
#     else:
#         print("It is a Prime Number")
# b=int(input("Enter a number to check whether it is prime or composite number: "))      
# prime_number(b)
# partition()
# #Q2. Find Palindrome of the given string.
# def palindrome(c):
#     c = str(c)  
    # d = c[::-1]  
#     if c == d:
#         print("Palindrome")
#     else:
#         print("Not palindrome")
# f=(input("Enter a number to check palindrome: "))
# palindrome(f)
# partition()

#Q3. Find Palindrome of the given string using loop 
def pali(k):
    l=[]
    for i in k:
        k.split()
        k.reverse()
        l.append(k)

pali("My name is Kartikay Jain ")