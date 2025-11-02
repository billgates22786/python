import random as rn


print(rn.randint(1,10))
print(rn.randrange(0,10,2))

print(rn.random())
print(rn.choice(["rock","paper","scissors"]))
print(rn.choices(["rock","paper","scissors"],k=2))

c=rn.choice(["rock","paper","scissors"])
u=input("Rock,Paper,Scissors")
print(c)
print(u)
if c==u:
    print("draw")
elif (c=="rock" and u=="paper") or (c=="paper" and u=="scissors") or (c=="scissors" and u=="rock"):
    print("u win")
elif c=="rock" and u=="scissors" or c=="paper" and u=="rock" or c=="scissors" and u=="paper":
    print("c win")
elif c=="paper" and u=="rock":
    print("c win")
elif c=="paper" and u=="scissors":
    print("u win")
elif c=="scissors" and u=="rock":
    print("u win")
elif c=="scissors" and u=="paper":
    print("c win")
else:
    print("invalid")


# import math

# print(math.factorial(5))
# print(math.log(5))
# print(math.pow(5,3))
# print(math.sqrt(25))
# print(math.pi)
# print(math.sin(90))
# print(math.cos(90))
# print()

# import time
# print(time.time())
# print(time.localtime())

# import calendar
# print(calendar.calendar(2024))
# print(calendar.isleap(2024))
# print(calendar.month(2024,9))
# print(calendar.monthrange(2024,9))




# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.now().day)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().year)