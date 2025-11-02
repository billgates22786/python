# lambda --> anonymous function 

# Syntax lambda arguments : expression

# def is_even(num):
#     if num % 2 == 0 :
#         return True
    
# print(is_even(12))

# is_even = lambda num : num % 2 == 0 
# print(type(is_even))
# print(is_even(12))z

# addition = lambda x,y,z : x+y+z
# print(addition(11,12,13))

# map(function, iterable)

lst = [1,2,3,4,5,6,7]
# for i in lst :
#     p=i+i
#     print(p)


squared = list(map(lambda i : i *2, lst))
print(squared)


string = ['1','2','3','4','5']
empty=[]
for i in string:
    empty.append(int(i))
print(type(empty))


we = list(map(lambda i : int(i), string))
print(we)

tsil=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda i : i%2==0, tsil)) ; print(even)


#Recursion       
# def age():
#     a=int(input("age "))
#     if 18<=a<=100:
#         print("hello")
#     else:
#         print("incorrect")
#         age()
# age()








