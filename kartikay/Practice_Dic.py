# k=int(input("Enter the number of states and city you want to input:"))
# all=[]
# state_name=[]
# city_name=[]
# for i in range(k):
#     p=input("Enter the State Name:")
#     c=input("Enter the city Name:")
#     state_name.append(p)
#     city_name.append(c)
#     all.append({"State_name":state_name[i],"City_name":city_name[i]})
    
# print(all)    
# Define the tuple
# t = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# # Get the value of k from the user
# k = int(input("Enter the value of k: "))

# # Rotate the tuple to the right by k positions
# # Use slicing to achieve the rotation
# rotated_t = t[-k:] + t[:-k]

# # Print the rotated tuple
# print("Rotated tuple:", rotated_t)


# # Given list
# list4 = [5, 10, 15, 20, 25, 30, 20, 35]

# # # Find and replace the first occurrence of 20 with 200
# # for i in range(len(list4)):
# #     if list4[i] == 20:
# #         list4[i] = 200
# #         break

# # # Output the updated list
# # print(list4)


# list4=[5, 10, 15, 20, 25, 30, 20, 35]
# print("Before replacement",list4)
# for i in range(8):
#     if list4[i]==20:
#         list4[i]=200

# print("After replacement",list4)
        
# print("Enter your choice:\n1.Rock (r)\n2.Paper (p)\n3.Scissor (s)")        
# z=input("Enter a string:")
# z=set(z)
# z=str(z)
# print("After Removing the duplicates the string:",z)



        
        
# for j in m:
#     l2.append(j)
    
# print(j)    

# l1=[1,2,3,4,[1,2,5,6,]]
# l2=[]
# for i in l1:
#     if type(i)==list:
#         for j in i:
#             l2.append(j)
#     else:
#         l2.append(i)        
            
# print(l2)
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# nums = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]

# for num in nums:
#     if is_prime(num):
#         print(f"{num} is Prime")
#     else:
#         print(f"{num} is Not Prime")

# class_subjects = {
#     "Kartikay": {"Maths", "English", "Physics"},
#     "Harman": {"English", "Punjabi", "Hindi"},
#     "Muskan": {"IT", "Maths", "Sociology"}
# }


# student_name = "Kartikay"
# subject_to_add = "Science"

# if student_name in class_subjects:
#     class_subjects[student_name].add(subject_to_add)
# else:
#     print(f"Student {student_name} not found.")
# student1 = "Kartikay"
# student2 = "Harman"

# if student1 in class_subjects and student2 in class_subjects:
#     common_subjects = class_subjects[student1].intersection(class_subjects[student2])
#     print(f"Common subjects between {student1} and {student2}: {common_subjects}")
# else:
#     print("One or both students not found.")
# print(class_subjects)


# class_subjects = {
#     "Kartikay": {"Maths", "English", "Physics"},
#     "Harman": {"English", "Punjabi", "Sociology"},
#     "Muskan": {"IT", "Maths", "Sociology"}
# }

# print("Enter the details of the student you want to edit")
# student_name = input("Enter Student name: ")
# Subject_add = input("Enter the subject to add: ")

# if student_name in class_subjects:
#     class_subjects[student_name].add(Subject_add)
#     print(f"Subject '{Subject_add}' added for {student_name}.")
# else:
#     print(f"Student '{student_name}' not found.")

# print("\nUpdated class subjects:", class_subjects)


# student1 = "Kartikay"
# student2 = "Harman"
# student3 = "Muskan"

# common = class_subjects[student1].intersection(class_subjects[student2]).intersection(class_subjects[student3])
# print(f"\nCommon Subjects Between {student1}, {student2}, and {student3}: {common}")


# Initial dictionary with student details (age and subjects)
# students = {
#     "Kartikay": {"age": 20, "subjects": {"Maths", "English", "Physics"}},
#     "Harman": {"age": 22, "subjects": {"English", "Punjabi", "Sociology"}},
#     "Muskan": {"age": 21, "subjects": {"IT", "Maths", "Sociology"}}
# }

# # Add a new subject to Kartikay's set of subjects
# new_subject = "Chemistry"
# if "Kartikay" in students:
#     students["Kartikay"]["subjects"].add(new_subject)

# # Update Harman's age
# new_age = 23
# if "Harman" in students:
#     students["Harman"]["age"] = new_age

# # Print all subjects Muskan is enrolled in
# if "Muskan" in students:
#     print(f"Muskan's subjects: {students['Muskan']['subjects']}")

# # Output the entire dictionary to check changes
# print(students)


# students = {
#     "Kartikay": {"age": 20, "subjects": {"Maths", "English", "Physics"}},
#     "Harman": {"age": 22, "subjects": {"English", "Punjabi", "Sociology"}},
#     "Muskan": {"age": 21, "subjects": {"IT", "Maths", "Sociology"}}
# }

# print("Enter Details to add new subject")
# student_name = input("Enter Student Name: ")
# new_subject = input("Enter the subject: ")
# students[student_name]["subjects"].add(new_subject)
# print(students)

# print("Enter Details to edit the age")
# student_name = input("Enter Student Name: ")
# new_age = int(input("Enter the new age: "))
# students[student_name]["age"] = new_age  # Correcting by directly assigning the value
# print(students)


# employee_details = {
#     101: {'name': 'John', 'department': 'HR', 'salary': 48000},
#     102: {'name': 'Alice', 'department': 'Finance', 'salary': 52000},
#     103: {'name': 'Bob', 'department': 'Engineering', 'salary': 60000},
#     104: {'name': 'David', 'department': 'Marketing', 'salary': 47000}
# }

# high_salary_employees = [details['name'] for details in employee_details.values() if details['salary'] > 50000]

# print(high_salary_employees)


# a = int(input("Enter a random number: "))
# print(f"Prime numbers from 1 to {a}:")

# if a > 1:
#     for i in range(2, a+1):
#         is_prime = True 
#         for j in range(2, int(i**0.5) + 1):  
#             if i % j == 0:  #
#                 is_prime = False
#                 break
#         if is_prime:
#             print(i, "is a Prime number")
#         else:
#             print(i, "is a Composite number")
# else:
#     print("Number should be greater than 1 to check for prime/composite.")

# dict1 = {}
# dict2 = {}


# q = int(input("How many numbers do you want to enter in dict1: "))
# for i in range(q):
#     c = input("Enter Key: ")
#     d = int(input("Enter Value: ")) 
#     dict1[c] = d
# r = int(input("How many numbers do you want to enter in dict2: "))
# for i in range(r):
#     e = input("Enter Key: ")
#     f = int(input("Enter Value: "))
#     dict2[e] = f
# print("Dictionary 1: ", dict1)
# print("Dictionary 2: ", dict2)
# merged_dict = dict1.copy()
# for key, value in dict2.items():
#     if key in merged_dict:
#         merged_dict[key] += value  
#     else:
#         merged_dict[key] = value  
# print("Merged Dictionary: ", merged_dict)