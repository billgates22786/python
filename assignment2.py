# main.py
import geometry

print("Choose shape to find area:")
print("1. Circle")
print("2. Rectangle")

choice = input("Enter choice (1/2): ")

if choice == '1':
    r = float(input("Enter radius: "))
    print("Area of circle =", geometry.area_circle(r))

elif choice == '2':
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area of rectangle =", geometry.area_rectangle(l, w))

else:
    print("Invalid choice!")
