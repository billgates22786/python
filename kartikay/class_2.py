class Car:
    def __init__(self) -> None:
        print(self)
        name = 'Bmw'
        color = 'spiderblack'
        print(f"My car is {name} and its color is {color}")
        
        
obj  = Car()
print(obj)


class Student:
    def __init__(self, name, roll_no) -> None:
        self.name = name
        self.roll_no = roll_no
        print(f"Welcome {self.name} and rollno {self.roll_no}")
        
    
        
        
s1  = Student("Raj",21)
s2 = Student("Rohan",25)


class Car2 :
    def __init__(self, user, name, model, color, tyre) -> None:
        self.user = user
        self.name = name
        self.model = model
        self.color= color
        self.tyre = tyre
        
    def car_info(self):
        print(f"Welcome {self.user} , You have selected {self.name}, with model {self.model}  , selected color is {self.color} and tyre size is {self.tyre}")
    
        
car1 = Car2("Jack",'Jeep','Rubicon','red',22)
car1.car_info()

class JeepRubicon:
    def __init__(self, model_year, engine, fuel_type, transmission, horsepower, torque, color, drive_type, price):
        self.model_year = model_year
        self.engine = engine
        self.fuel_type = fuel_type
        self.transmission = transmission
        self.horsepower = horsepower
        self.torque = torque
        self.color = color
        self.drive_type = drive_type
        self.price = price

    def display_details(self):
        print(f"Jeep Rubicon {self.model_year} Details:")
        print(f"Engine: {self.engine}")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Transmission: {self.transmission}")
        print(f"Horsepower: {self.horsepower} hp")
        print(f"Torque: {self.torque} lb-ft")
        print(f"Color: {self.color}")
        print(f"Drive Type: {self.drive_type}")
        print(f"Price: ${self.price:,}")
jeep_rubicon = JeepRubicon(
    model_year=2024, 
    engine="3.6L V6", 
    fuel_type="Gasoline", 
    transmission="8-speed automatic", 
    horsepower=285, 
    torque=260, 
    color="Black", 
    drive_type="4x4", 
    price=45000
)

jeep_rubicon.display_details()

# class School:
#     def __init__(self,name,roll_no,sub1,sub2,sub3):
#         self.name = name
#         self.roll_no = roll_no
#         self.sub1 = sub1
#         self.sub2 = sub2
#         self.sub3 = sub3
#     def display(self):
#         average=(self.sub1+self.sub2+self.sub3)/3
#         print(f"The Student name {self.name} of roll no {self.roll_no} and the average marks of the student in all the three subjects are {average}")

# s1 = School("Kartikay",21,50,50,50)
# s1.display()

class School:
    def __init__(self, name, roll_no, sub1):
        self.name=name
        self.roll_no=roll_no
        self.sub1=sub1  
    
    def display(self):
        total = sum(self.sub1)  
        average = total /3 
        print(f"The student name is {self.name}, roll no: {self.roll_no}, and the average marks in all subjects are {average}")
        
s1 = School("Kartikay", 21, [55, 65, 85])
s1.display()

