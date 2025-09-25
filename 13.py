# Series evaluation
import math
x = float(input("Enter x: "))
n = int(input("Enter n: "))
sum1 = 0
for i in range(1, n+1):
    sum1 += ((-1)**(i+1)) * (x**i) / math.factorial(i)
print("Series a:", sum1)

sum2 = 0
for i in range(1, n+1, 2):
    sum2 += ((-1)**((i-1)//2)) * (x**i) / math.factorial(i)
print("Series b:", sum2)