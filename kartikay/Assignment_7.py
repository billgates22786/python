def partition():
    print(" ")
    print("********************************************************************************************************************************************************************************************")
    print(" ")
# 1. Write a function that takes a list and returns a new list with distinct elements from the first list.
#       [1,2,3,3,3,3,4,5] [1, 2, 3, 4, 5]
def unique():
    unique_list = []
    n = int(input("How many numbers you want to enter: "))
    for i in range(n):
        k = int(input(f"Enter a {i+1} number: "))
        if k not in unique_list:
            unique_list.append(k)
    print(unique_list)
unique()
partition()
# 2.Write a function to multiply all the numbers in a list.: (8, 2, 3, -1, 7) 
#  : -336
def multiply_numbers():
    numbers = []
    n = int(input("How many numbers do you want to enter: "))
    for i in range(n):
        k = int(input(f"Enter number {i+1}: "))
        numbers.append(k)
    product = 1
    for i in numbers:
        product *= i
    print("The product of the numbers is:", product)
multiply_numbers()
partition()
# 3. Write a function to find the largest item from a given list:
#       list=[4, 6, 8, 24, 12, 2]
def largest():
    list2 = []
    n = int(input("How many numbers do you want to enter: "))
    for i in range(n):
        k = int(input(f"Enter number {i + 1}: "))
        list2.append(k)
    num = list2[0] 
    for i in list2[1:]:
        if i > num:
            num = i  
    print("The largest number is:", num)
largest()
partition()

# 4 Write a function to Take multiple values from user and return there product
def multiply_numbers():
    numbers = []
    n = int(input("How many numbers do you want to enter: "))
    for i in range(n):
        k = int(input(f"Enter number {i+1}: "))
        numbers.append(k)
    product = 1
    for i in numbers:
        product *= i
    print("The product of the numbers is:", product)
multiply_numbers()
partition()
