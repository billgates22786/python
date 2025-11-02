#STRINGS
#Q1. Write a script that reverses the words in a given sentence sentence and prints the reversed sentence. 
# For example, for "Hello World", it should print "World Hello".
k="Hello World"
s=k.split()[::-1]
l=[]
for i in s:
    l.append(i)
    
print(l)        

#Q2 Write a script that removes duplicates from a list lst while preserving the original order of elements and prints the result.
z=input("Enter a string:")
z=set(z)
z=str(z)
print("After Removing the duplicates the string:",z)




#Q3 Write a script that flattens a nested list nested_list (a list that can contain other lists) into a single list of elements 
# and prints the flattened list.
l1=[1,2,3,4,[1,2,5,6,]]
l2=[]
for i in l1:
    if type(i)==list:
        for j in i:
            l2.append(j)
    else:
        l2.append(i)        
            
print(l2)
            