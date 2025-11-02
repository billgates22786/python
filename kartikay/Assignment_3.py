#Q1.Ask user to input a string and tell us total occurence of vowels in string.
# x=input("Enter a string: ")
# a=0
# vowels="aeiouAEIOU"
# for i in x:
#     if i in vowels:
#         a+=1

# print("Total occurence of vowels:",a)  
# for i in x:
#     if i=="a" or i=="e":
#         a=a+1

# print(a)      


#Q2Ask user to input a string and tell total vowels along with each voweloccurence
# eg:
#     Enter String: My Name is Sharma G Jalandhar wale
#     Total Vowel: 10
#     a-
#     e-1
#     i-1
#     o-0
#     u-
# y=input("Enter a String: ")
# a=0
# e=0
# j=0
# o=0
# u=0

# for i in y:
#     if i =="a" or i =="A":
#         a=a+1
#     if i=="e" or i=="E":
#         e=e+1
#     if i=="i" or i=="I":
#         j=j+1    
#     if i=="o" or i=="O":
#         o=o+1
#     if i=="u" or i=="U":
#         u=u+1    
# print("Total occurence of vowel a:",a)
# print("Total occurence of vowel e:",e)
# print("Total occurence of vowel i:",j)
# print("Total occurence of vowel o:",o)
# print("Total occurence of vowel u:",u)


#Q3.Perform the above question again but without using any inbuild function
# Already done above


#Q4.  Ask user to input a String and find out the 2nd occurenace of character a
# example:
#     String is:   Gursagar Singh
#                  01234567890123
#     2nd a ;location is 6
# string = input("Enter a string: ")
# first = string.find('a')
# second = string.find('a',first+1)
# if second != -1:
#     print(f"Second 'a' location is {second}")
# else:
#     print("There is no second 'a' in the above string.")


#Q5. Ask user to input a string and enter character i 5 times and tell location/index of last i
# example:   India is a country in asia where we all live
#            01234567890123456789012345678901234567890123
#            Last i location is 41

# x=input("Enter Random String: ")
# print("Last I location is",x.rfind("i"))


#Q6. Ask user to input a string and tell
# a. total characters in string
# b. total character in string not including space
# c. total character a in the string
# d. total digits in the string


# m = input("Enter a string: ")
# print("Total characters in string:", len(m))
# print(f"Total characters in string not including spaces: {len(m)-m.count(' ')}")
# a=0
# for i in m:
#     if i=="a" or i=="A":
#         a=a+1
        
# print("The total character a in string",a) 
# k = 0
# for i in m:
#     if i.isdigit():
#         k=k+1
# print("Total digits in the string:",k)


#Q7. Ask user to input 3 numbers a,b,c and tell who is greater in all using logical operators
# a=int(input("Enter First Number: "))
# b=int(input("Enter Second Number: "))
# c=int(input("Enter third Number: "))
# if a>b:
#     print(a,"is greater")
# elif b>c:
#     print(b,"is greater")
# elif c>a:
#     print(c,"is greater")


#Q8. Ask user to input a number and print allow if that number fully divisible by any of following number 10,5,3
# kk=int(input("Enter your number:"))
# if kk%10==0 or kk%5==0 or kk%3==0:
#     print(kk)
    