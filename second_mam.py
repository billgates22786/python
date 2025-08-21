import math 
radius=float(input("Enter the radius of the circle: "))
circle=math.pi*radius**2
print(f"Area of circle: {circle}")

length=float(input("Enter the length of the rectangle: "))
breadth=float(input("Enter the breadth of the rectange: "))
rectangle=length*breadth
print(f"Area of square: {rectangle}")

base=float(input("Enter the base of the triangle: "))
height1=float(input("Enter the height of the triangle: "))
triangle=0.5*base*height1
print(f"Area of triangle: {triangle}")

side=float(input("Enter the side of the square: "))
square=side**2
print(f"Area of square: {square}")

base1=float(input("Enter the base1 of the trapezoid: "))
base2=float(input("Enter the base2 of the trapezoid: "))
height2=float(input("Enter the height of the trapezoid: "))
trapezoid=0.5*(base1+base2)*height2
print(f"Area of the trapezoid: {trapezoid}")

base3=float(input("Enter the base of the parallelogram: "))
height3=float(input("Enter the height of the parallelogram: "))
parallelogram=base3*height3
print(f"Area of the parallelogram: {parallelogram}")