# Types of function :
# 1 ). Predefine
# 2). Userdefine
# 3). Anonymous

# 1 ). print(), len(), min(), max()

# Syntax of function:
# def function_name(parameters):
#     block of code
    
# function call(arguments)


# a = 10
# b = 20
# print(a + b)

# def greet():
#     print("Hi Good morning")
    
# greet()
 
# def greet():
#     pass

# def additions(a, b):
#     print(a + b)
    
# additions(12,11)

# def additon2(a, b, c):
#     print(a + b+c)
    
# additon2(11,12,13)

# def info(name, age):
    
#     print(f"My name is {name} and my age is {age}.")
    

# name2 = input("Enter your name :")
# age2 = int(input("Enter your age :"))

# info(name2, age2)

# Types of Arguments:
# 1). Required Arguments
# def sub(a, b):
#     print(a - b)


# sub(11,12)    
# sub(1,2,3)

# 2). Default Argumets

# def college_name(college="DAV"):
#     print(f"My college is {college}")
    
# college_name()
# college_name("PTU")


# 3). Keyword Arguments


# def info(name, age):
#     print(f"My name is {name} and i am {age} years old,")
    
# info(22, "Ram")
# info(age=22, name="Ram")
# info("Shyam", age=22)
# info(age=22, "HARI")




# def info(name, age, occup):
#     print(f"My name is {name} and i am {age} years old and job is {occup}")
    
# info(name="Barry", 23, occup="Python")

# Variable length
# *args, **kwargs

# def sum(*args):
#     print(type(args))
#     y = 0
#     for x in args:
#         y += x
#     print(y)

# sum(12,13)
# sum(11,12,3,45,55)
# sum(157, 3)


# def data(**kwargs):
#     print(type(kwargs))
#     for x, y in kwargs.items():
#         print(f"{x}:{y}")
    
    
# data(name="abhi", age=21, occpation='Developer')
# data(Name="L", age=22)


# def info(name, *args):
#     sum = 0
#     for x in args:
#         sum += x
#     print(f"Welcome {name} sum of numbers {sum}")
    
# info("hhh",12,12)
# info()


def is_palindrome(string):
    string = string.lower().replace(" ","")
    # return string == string[::-1]
    start = 0
    end = len(string)-1
    
    while start < end :
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
        
    return True

input_str  = "hahhha"
if is_palindrome(input_str):
    print(f"{input_str} is a Palindrome")
else :
    print(f"{input_str} not a Palindrome")