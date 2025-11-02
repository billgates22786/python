print("Trip planner by Krox Pvt Ltd")
x = int(input("Enter your Budget: "))

if (100000 <= x <= 200000):
    print("The countries in your budget are:\n 1. Thailand\n 2. Vietnam\n 3. Nepal")
    y = int(input("Enter the country number you want to visit: "))
    if y == 1: 
        print("The famous locations in Thailand:\n 1. Bangkok\n 2. Chiang Mai\n 3. Pattaya")
    elif y == 2:
        print("The famous locations in Vietnam:\n 1. Hanoi\n 2. Ho Chi Minh City\n 3. Ha Long Bay")
    elif y == 3:
        print("The famous locations in Nepal:\n 1. Kathmandu\n 2. Pokhara\n 3. Chitwan")
elif (200000 < x <= 300000):
    print("The countries in your budget are:\n 1. Japan \n 2. Australia\n 3. New zealand")
    y = int(input("Enter the country number you want to visit: "))
    if y == 1: 
        print("The famous locations in Japan:\n 1.Tokyo\n 2. Kyoto\n 3. Osaka")
    elif y == 2:
        print("The famous locations in Australia:\n 1. Melbourne\n 2. Sydney\n 3. Barrier Reef")
    elif y == 3:
        print("The famous locations in New Zealand:\n 1. Auckland\n 2. Wellington\n 3. QueenTown")
elif (300000 < x <= 400000):
    print("The countries in your budget are:\n 1.Western Europe \n 2. United Kingdom\n 3.USA")
    y = int(input("Enter the country number you want to visit: "))
    if y == 1: 
        print("The famous locations in Western Europe:\n 1.Paris\n 2. Rome\n 3. Berlin")
    elif y == 2:
        print("The famous locations in United Kingdom:\n 1. London\n 2. Scootland\n 3. Greenland")
    elif y == 3:
        print("The famous locations in USA:\n 1. New York\n 2. Washington\n 3. Los Angels")
elif (400000 < x <= 500000):
    print("The countries in your budget are:\n 1. Italy \n 2. France\n 3. Switzerland")
    y = int(input("Enter the country number you want to visit: "))
    if y == 1: 
        print("The famous locations in Italy:\n 1.Venice\n 2. Florence\n 3. Amalfi coast")
    elif y == 2:
        print("The famous locations in France:\n 1. Riviera\n 2. Loire\n 3. Bangesim")
    elif y == 3:
        print("The famous locations in Switzerland:\n 1. Zurich\n 2.Lucerne\n 3. Swiss Alps")     
else:
    print("WE dont have any options in your certain budget ")                   

