# Part 1: Conditional Statements (3 Questions) 
import partition as p 
p.partition()
#Q1.Write a Python function is_even(num) that takes an integer num as input and returns True if it is even, and False otherwise. 
def even_odd(i):
    if i%2==0:
        print(i,"is Even Number")
    else:
        print(i,"is Odd Number")
even_odd(11)
p.partition()
#Q2.Create a function grade(score) that takes a score (0-100) as input and returns a letter grade:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: below 60
def grade(score):
    if 90<=score<=100:
        return 'A'
    elif 80<=score<90:
        return 'B'
    elif 70<=score<80:
        return 'C'
    elif 60<=score<70:
        return 'D'
    else:
        return 'F'
print("The grade is:", grade(55))
p.partition()
#Q3.Write a function check_leap_year(year) that checks if a given year is a leap year. A year is a leap year if:
# It is divisible by 4,
# It is not divisible by 100 unless it is also divisible by 400.
def leap_year(n):
   if n%4==0 and n%100!=0:
       print(n,"Leap Year")
   else:
       print("Non Leap Year")   
k=int(input("Enter the year: "))     
leap_year(k)
p.partition()
# Part 2: Loops (3 Questions) 
#Q1. Write a function sum_of_numbers(n) that returns the sum of all integers from 1 to n (inclusive) using a loop. 
def sum_of_numbers(n):
    a=0
    for i in range(1, n+1):
        a+=i
    print(a)
n = int(input("Enter a number: "))
sum_of_numbers(n)
p.partition()
#Q2. Create a function fizz_buzz(n) that prints the numbers from 1 to n, but for multiples of 3 print "Fizz", 
# for multiples of 5 print "Buzz", and for multiples of both 3 and 5 print "FizzBuzz". 
def fizz_buzz(n):
    for i in range(1, n+1):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
fizz_buzz(10)
p.partition()
#Q3. Write a function count_vowels(s) that takes a string s and returns the number of vowels (a, e, i, o, u) in it, using a loop.
def count_vowels(s):
    count=0
    for j in k:
        if j=="a" or j=="A" or j=="e" or j=="E" or j=="i" or j=="I" or j=="o" or j=="O" or j=="u" or j=="U":
            count+=1
    print("Number of vowels in the string",count)
k=input("Enter a random string: ")
print("Vowels: a,e,i,o,u")
count_vowels(k)

# Part 3:Lists (3 Questions) 
#Q1. Write a function reverse_list(lst) that takes a list and returns a new list with the elements in reverse order.
def reverse_list(list):
    reversed_list=[]
    for i in list(-1):
        reverse_list.append(i)
        print(reverse_list)
my_list=[1,2,3,4,5]
print(reverse_list(my_list))
p.partition()
#Q2. Create a function remove_duplicates(lst) that takes a list and returns a new list with duplicates removed, 
# preserving the original order of elements. 
def remove_duplicates(lst):
    new=set()  
    unique_list = [] 
    for i in lst:
        if i not in new:  
            unique_list.append(i)  
            new.add(i)  
    print(unique_list)  
my_list2=[1,1,2,4,2,5,64,754,8,6,86]
print(remove_duplicates(my_list2))
p.partition()
#Q3. Write a function find_max(lst) that takes a list of numbers and returns the maximum value
def find_max(star):
    max_value=star[0]
    for i in star:
        if i>max_value:
            max_value=i
        print(max_value)
list3=[25,855,69,74,25,1475,25,30,74]
print(find_max(list3))
p.partition()
# Part 4:Dictionaries (3 Questions) 
#Q1. Write a function count_occurrences(lst) that takes a list and returns a dictionary with the count of each element. 
def count_occurrences(lst):
    occurrence_dict={}
    for i in lst:
        if i in occurrence_dict:
            occurrence_dict[i] += 1
        else:
            occurrence_dict[i] = 1
    print(occurrence_dict)
count_occurrences_list = []
p = int(input("How many numbers do you want to enter: "))
for i in range(p):
    b = int(input(f"Enter number {i+1}: "))
    count_occurrences_list.append(b)
occurrences = count_occurrences(count_occurrences_list)
print("Entered numbers:", count_occurrences_list)
print("Count of each element:", occurrences)
p.partition()
#Q2. Create a function merge_dicts(dict1, dict2) that takes two dictionaries and returns a new dictionary that combines them. 
# If there are duplicate keys, sum their values.
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key]+=value
        else:
            merged_dict[key]=value
    return merged_dict
dict1={}
dict2={}
q=int(input("How many numbers do you want to enter in dict1: "))
for i in range(q):
    c=input("Enter Key: ")
    d=int(input("Enter Value: ")) 
    dict1[c]=d
r=int(input("How many numbers do you want to enter in dict2: "))
for i in range(r):
    e=input("Enter Key: ")
    f=int(input("Enter Value: "))  
    dict2[e]=f
print("Dictionary 1: ", dict1)
print("Dictionary 2: ", dict2)
merged_dict=merge_dicts(dict1, dict2)
print("Merged Dictionary: ", merged_dict)

# Part 5:Tuples and Sets (3 Questions)
#Q1. Write a function tuple_to_list(t) that converts a tuple t to a list and returns the list. 
def tuple_to_list(t):
    print(list(t))
a=(1,2,3,4,5,6)
convert=tuple_to_list(a)
print(convert)
#Q2. Create a function intersection(set1, set2) that takes two sets and returns a set that contains the common elements. 
def intersection(set1, set2):
    print(set1.intersection(set2))
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
common_elements = intersection(set1, set2)
print(common_elements)

#Q3. Write a function unique_elements(lst) that takes a list and returns a set of unique elements from that list.
def unique_elements(w):
    print(set(w))
list5=[1,2,2,3,4,4,5,6,8,7,2]
unique_set=unique_elements(list5)
print(unique_set)
