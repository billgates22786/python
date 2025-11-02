#conditional statement

#if condition:
#    block of code

# a=int(input("enter age "))

# if a>=18:
#     print("you can vote")

#if else
#if condition:
#    block of code
#else:
#    block of code

# a=int(input("enter age "))
# if a>=18:
#     print("you can vote")
# else:
#     print("you cannot vote")



#if elif else
#if condition:
#    block of code
#elif condition:
#    block of code
#elif condition:
#    block of code
#else:
#    block of code


# x=input("enter course ")

# if x=="Med":
#     print("doctor")

# elif x=="non med":
#     print("engineer")

# elif x=="com":
#     print("canada")

# elif x=="arts":
#     print("physology")

# else:
#     print("sanu nhi pata")

# y=int(input("enter number "))

# if y<4 and y>0:
#     print("less than 4 and greater than 0")

# elif y==4:
#     print("equal to 4")

# elif y>4 and y<8:
#     print("greater than 4 and less than 8")

# elif y>10 or y<7:
#     print("greater than 10 or less than 7")

# else:
#     print("greater than 8")



#nested if

# if condition:
#     block of code
#     if condition:
#         block of code
#     else:
#         block of code
# else:
#     block of code

a=input("kithe jana ")


if a=="tan cafe":
    b=input("veg or non veg")
    if b=="veg":
        c=input("ki khana")
        if c=="pasta":
            print("500")
        elif c=="pizza":
            print("1000")
        else:
            print("panni")

    elif b=="non veg":
        c=input("ki khana")
        if c=="chicken":
            print("500")
        elif c=="mutton":
            print("1000")
        else:
            print("panni")

elif a=="zoka":
    b=input("veg or non veg")
    if b=="veg":
        c=input("ki khana")
        if c=="dumplen":
            print("500")
        elif c=="pasta":
            print("400")
        else:
            print("panni")

    elif b=="non veg":
        c=input("ki khana")
        if c=="chicken":
            print("500")
        elif c=="mutton":
            print("1000")
        else:
            print("panni")

elif a=="starbucks":
    b=input("veg or vegan ")
    if b=="vegan":
        c=input("ki khana")
        if c=="badam vala dudh with coffe":
            print("700")
        else:
            print("panni")

    elif b=="veg":
        c=input("ki khana")
        if c=="coffee":
            print("500")
        elif c=="shake":
            print("800")
        else:
            print("panni")

else:
    print("zomato")