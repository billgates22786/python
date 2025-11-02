# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def divide(x, y):
#     if y == 0:
#         return "Cannot divide by zero!"
#     else:
#         return x / y

# def multiply(x, y):
#     return x * y

# def power(x, y):
#     return x ** y

# def remainder(x, y):
#     return x % y

# def calculator():
#     print("Welcome to Sada Calculator")
    
#     while True:
#         print("\nSelect your choice:")
#         print("1. Addition")
#         print("2. Subtraction")
#         print("3. Division")
#         print("4. Multiplication")
#         print("5. Power")
#         print("6. Remainder")
#         print("7. Exit")
        
#         choice = input("Enter your choice (1-7): ")
        
#         if choice == '7':
#             print("Exiting the calculator. Goodbye!")
#             break
        
#         if choice in ['1', '2', '3', '4', '5', '6']:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
            
#             if choice == '1':
#                 print(f"The result of addition is: {add(num1, num2)}")
#             elif choice == '2':
#                 print(f"The result of subtraction is: {subtract(num1, num2)}")
#             elif choice == '3':
#                 print(f"The result of division is: {divide(num1, num2)}")
#             elif choice == '4':
#                 print(f"The result of multiplication is: {multiply(num1, num2)}")
#             elif choice == '5':
#                 print(f"The result of power is: {power(num1, num2)}")
#             elif choice == '6':
#                 print(f"The result of remainder is: {remainder(num1, num2)}")
#         else:
#             print("Invalid choice. Please select a number between 1 and 7.")

# # Run the calculator
# calculator()
y = input("Enter a String: ")

# Counting occurrences of vowels using the count() method
a = y.lower().count("a")
e = y.lower().count("e")
j = y.lower().count("i")
o = y.lower().count("o")
u = y.lower().count("u")

print("Total occurrence of vowel a:", a)
print("Total occurrence of vowel e:", e)
print("Total occurrence of vowel i:", j)
print("Total occurrence of vowel o:", o)
print("Total occurrence of vowel u:", u)
