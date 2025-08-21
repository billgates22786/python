import cmath
a=int(input("Enter a number (a): "))
b=int(input("Enter a number (b): "))
c=int(input("Enter a number (c): "))
discriminant=b**2-4*a*c
root1=(-b+cmath.sqrt(discriminant))/(2*a)
root2=(-b-cmath.sqrt(discriminant))/(2*a)
print(f"Root 1: {root1}")
print(f"Root 2: {root2}")