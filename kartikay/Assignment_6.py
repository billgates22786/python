#Q1. Find all of the numbers from 1-1000 that are divisible by 7
print("All of the numbers from 1-1000 that are divisible by 7 ")
for i in range(1, 1001):  
    if i % 7 == 0:         
        print(i)       
             
#Q2. Count the number of spaces in a string
x=input("Enter a random string:")
space=x.count(' ')
print("number of spaces in string",space)

#Q3. Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
list_a=[1,2,3,4]
list_b=[2,3,4,5]
common=[i for i in list_a if i in list_b]
print("Common Elements:",common)

#Q4Produce a list of tuples consisting of only the matching numbers in these lists 
# list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)

#Q5 Find all of the words in a list of string that are less than 4 letters
a=["my name is kartikay"]
split=[]
four=[]
for i in a:
    words=i.split()
    
print(words)   
for i in words: 
    if len(i)<4:
        four.append(i)

print(four)    

#Q6 Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, 
# and the word ‘odd’ if the number is odd. Result would look like ‘odd’,'even',........    
result = []
for i in range(20):
    k=int(input("Enter the number:"))
    if i % 2 == 0:
        result.append('even')
    else:
        result.append('odd')

print(result)

#Q7 Concatenate two lists in the following order
# Given list1 - [‘hello’, ‘o7’]    
# Given list2 - [‘world’, ‘services’]
# Output - [‘hello world’, ‘hello services’, ‘o7 world’, ‘o7 services’]     
list1=['hello','O7']
list2=['world','services']
all=[]
for i in range(1):
    all.append(f'{list1}{list2}')

print(all)

#Q8Add 10 to list after a 600
# Given list - [10, 20, [300, 400, [5000, 600], 500], 30, 50]
# Output - [10, 20, [300, 400, [5000, 600, 10], 500], 30, 50]
list3=[10,20,[300,400,[5000,600],500],30,50]
list3[2][2].insert(600,10)
print(list3)

#Q9. You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
# Given list - [5, 10, 15, 20, 25, 30, 20, 35]
# Output - [5, 10, 15, 200, 25, 30, 20, 35]
list4=[5, 10, 15, 20, 25, 30, 20, 35]
print("Before replacement",list4)
for i in range(8):
    if list4[i]==20:
        list4[i]=200

print("After replacement",list4)
        
        