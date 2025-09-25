# cook your dish here
lst = [2, 4, 6, 8, 10]

lst.append(12) #This line appends 12 at the end of the lst 
print(lst)
#List becomes [2, 4, 6, 8, 10, 12]

lst.insert(2, 5)  #This line inserts the element 5 at position 2 
print(lst)
#List becomes [2, 4, 5, 6, 8, 10, 12]

more_elements = [14, 16, 18, 20]
lst.extend(more_elements) #This adds the elements of more_elements to the lst 
print(lst)
#List becomes [2, 4, 5, 6, 8, 10, 12, 14 , 16, 18, 20]