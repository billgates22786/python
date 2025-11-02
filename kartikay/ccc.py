try:
  n1=int(input("Enter first number = "))
  n2=int(input("Enter second number = "))
  result=n1/n2
except ZeroDivisionError as Z:
  print(Z)
except ValueError as V:
  print(V)
except KeyboardInterrupt as K:
  print(K)
else:
  print(result)
finally:
  print("End of the program")
