import math

# Function to compute area of different shapes
def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_square(side):
    return side ** 2

def area_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def area_parallelogram(base, height):
    return base * height

# Sample Inputs
print("Areas of Various Shapes:")
print(f"Circle (radius=5): {area_circle(5):.2f}")
print(f"Rectangle (length=10, width=4): {area_rectangle(10, 4)}")
print(f"Triangle (base=6, height=3): {area_triangle(6, 3)}")
print(f"Square (side=4): {area_square(4)}")
print(f"Trapezoid (base1=5, base2=7, height=4): {area_trapezoid(5, 7, 4)}")
print(f"Parallelogram (base=8, height=5): {area_parallelogram(8, 5)}")
