# Tuples 
#Q1.Write a script that takes a tuple t of integers and calculates and prints the sum of the elements in the tuple.
tu=(1,2,3,4,5,6,7,8,9,10)
j=0
for i in tu:
    j +=i
    
print("Sum of the elements in tuple:",j)   

#Q2. Write a script that rotates the elements of a tuple t to the right by k positions, 
# where k is provided by the user, and prints the rotated tuple.
t=(1,2,3,4,5,6,7,8,9)
k=int(input("Enter the value:"))
rotate=t[-k:] + t[:-k]
print("After rotate",rotate)




#sets 
# Write a script that finds and prints the common elements between two sets set1 and set2. 
# Write a script that finds and prints the elements that are in set1 but not in set2
set1={1,2,3,4,5,6,7,8,9}
set2={4,5,6,7,8,9}
print("Common elements in both the sets are:",set1.intersection(set2))
print("The elements which are in set a but not in set b",set1.difference(set2))


# Dictionaries
#  Write a script that inverts a dictionary d (swapping keys and values) and prints the inverted dictionary. 
# Assume that the original dictionary values are unique.
d={"name":"kartikay",
   "age":22,
    13:True,
   "roll no":123,
   "section":"A",
   "section":"B",
   }
print("After swapping keys and values")
for i in d:
    print(d[i],i)
    
