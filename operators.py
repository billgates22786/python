# Comparision Operator 
a=10
b=5
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)

# Logical operators
for i in range(10,0,-1):
    print(i,end=" ")
    
# Membership operators
x=20
y=58
x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
new=[10,20,30,40,50]
if x in new:
    print(f"The value {x} is present")
elif y in new:
    print(f"The value {y} is present")
else:
    print("The value of x and y both is not present")

