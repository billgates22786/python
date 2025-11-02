# Q1. Write a reverse_list(lst) that takes a list and returns a new list with the elements in reverse order.
reverse_list = []
n=int(input("How many numbers do you want to enter: "))
for i in range(n):
    k=int(input(f"Enter number {i+1} : "))
    reverse_list.append(k)
reverse_list.reverse()
print("Reversed List:",reverse_list)


#Q2.Create remove_duplicates(lst) that takes a list and returns a new list with duplicates removed, preserving the original order of elements. 
remove_duplicates = []
m=int(input("How many numbers do you want to enter: "))
for i in range(m):
    l=int(input(f"Enter number {i+1}: "))
    remove_duplicates.append(l)
new=[]
sets=set()
for j in remove_duplicates:
    if j not in sets:
        new.append(j)
        sets.add(j)
print("List after removing duplicates:", new)


#Q3. Write a without function find_max(lst) that takes a list of numbers and returns the maximum value.
find_max=[]
o=int(input("How many numbers do you want to enter: "))
for i in range(o):
    a=int(input(f"Enter number {i+1}: "))
    find_max.append(a)
max_num=find_max[0]
for j in find_max:
    if j > max_num:
        max_num = j
print("Maximum value:", max_num)


#Q4. Write a function count_occurrences(lst) that takes a list and returns a dictionary with the count of each element
count_occurrences = []
p=int(input("How many numbers do you want to enter: "))
for i in range(p):
    b=int(input(f"Enter number {i+1}: "))
    count_occurrences.append(b)
occurrence_dict={}
for j in count_occurrences:
    if j in occurrence_dict:
        occurrence_dict[j]+=1
    else:
        occurrence_dict[j]=1
print("Entered numbers:", count_occurrences)
print("Count of each element:", occurrence_dict)


#Q5. Create a function merge_dicts(dict1, dict2) that takes two dictionaries and returns a new dictionary that combines them. 
# If there are duplicate keys, sum their values. 
dict1={}
dict2={}
q=int(input("How many numbers do you want to enter in dict1: "))
for i in range(q):
    c=input("Enter Key:")
    d=input("Enter value:")
    dict1[c]=d
r=int(input("How many numbers do you want to enter in dict2: "))
for i in range(r):
    e=input("Enter Key:")
    f=input("Enter value:")
    dict2[e]=f
print("Dictionary 1: ",dict1)
print("Dictionary 2: ",dict2)
merged_dict = dict1.copy()
for key,value in dict2.item(): # hint took from google 
    if key in merged_dict:
        merged_dict[key]+=value  
    else:
        merged_dict[key]=value  
print("Merged Dictionary: ", merged_dict)


#Q6. Write a tuple_to_list(t) that converts a tuple t to a list and returns the list 
tuple_to_list=[]
t = (1, 2, 3, 4, 5) 
tuple_to_list=list(t)
print(tuple_to_list)

#Q7. Create a function intersection(set1, set2) that takes two sets and returns a set that contains the common elements. 
set1={1,2,3,4,5,6,7,8,9}
set2={4,5,6,7,8,9}
print("Common elements in both the sets are:",set1.intersection(set2))


#Q8. Write a function unique_elements(lst) that takes a list and returns a set of unique elements from that list.
unique_elements = []
u=int(input("How many numbers do you want to enter: "))
for i in range(m):
    l=int(input(f"Enter number {i+1}: "))
    unique_elements.append(l)
new=[]
sets=set()
for j in remove_duplicates:
    if j not in sets:
        new.append(j)
        sets.add(j)
print("List with unique elements:", new)