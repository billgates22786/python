#  Q1. 
# Create a list of dictionaries where each dictionary represents a student with keys: name, age, and score.
# Iterate through the list and print each student's name and score.
# Add a new dictionary for a new student to the list.
# Creating a list of dictionaries representing students
students = [
    {"Name":"Kartikay Jain","Age":18,"Score":80},
    {"Name":"Naruto","Age":60,"Score":90},
    {"Name":"Sakura","Age":55,"Score":88}
]
for i in students:
    print(f"Name:{i['Name']},Score:{i['Score']}")
new={"name": "David", "age": 23, "score": 92}
students.append(new)
print(students)


# Q2.
# Create a dictionary class_subjects where keys are student names and values are sets of subjects they are enrolled in.
# Add a new subject to a student's set of subjects.
# Find the intersection of subjects between two students.
# # Initialize the dictionary
class_subjects={
    "Kartikay":{"Maths","English","Physics"},
    "Harman":{"English","Punjabi","Sociology"},
    "Muskan":{"IT","Maths","Sociology"}
}
print("Enter the details of the student you want to edit")
student_name=input("Enter Student name: ")
Subject_add=input("Enter the subject to add: ")
# student_name="Kartikay"
# Subject_add="Science"
if student_name in class_subjects:
    class_subjects[student_name].add(Subject_add)

print("Updated data after the edit: ",class_subjects)

student1="Kartikay"
student2="Harman"
student3="Muskan"
common=class_subjects[student1].intersection(class_subjects[student2]).intersection(class_subjects[student3])

print("Common Subjects Between Kartikay,Harman and Muskan:",common)    

    
    




#Q3.
# Create a dictionary where the keys are student names and the values are dictionaries containing age and subjects (a set of subjects).
# Add a new subject to a student's set of subjects.
# Update a student's age.
# Print the list of all subjects a particular student is enrolled in.
students = {
    "Kartikay": {"age": 20, "subjects": {"Maths", "English", "Physics"}},
    "Harman": {"age": 22, "subjects": {"English", "Punjabi", "Sociology"}},
    "Muskan": {"age": 21, "subjects": {"IT", "Maths", "Sociology"}}
}

print("Enter Details to add new subject")
student_name = input("Enter Student Name: ")
new_subject = input("Enter the subject: ")
students[student_name]["subjects"].add(new_subject)
print(students)

print("Enter Details to edit the age")
student_name = input("Enter Student Name: ")
new_age = int(input("Enter the new age: "))
students[student_name]["age"] = new_age 
print(students)




#Q4.
# Given a dictionary employee_details where the keys are employee IDs and values are dictionaries with 
# name, department, and salary, filter and create a list of names of employees who have a salary greater than 50,000.
employee_details = {
    420: {'name': 'Tanishq', 'department': 'HR', 'salary': 48988},
    786: {'name': 'Dev', 'department': 'Finance', 'salary': 52589},
    140: {'name': 'Sehaj', 'department': 'Engineering', 'salary': 60789},
    960: {'name': 'Pranav', 'department': 'Marketing', 'salary': 47874}
}
print("Employees with salary greater than 50000: ")
details=['name']
for details in employee_details.values():
    if details['salary']>50000:
        print(details)
        
        