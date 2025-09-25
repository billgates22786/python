# cook your dish here
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst.remove(2)
#This removes the integer 2 from the list 
print(lst)

lst.pop(0)
#This removes the integer at the 0 index in the list
print(lst)

lst.pop()
#This removes the last element of the list
print(lst)

del lst[0]
#This deletes the first index of the list
print(lst)

del lst
#This deletes the whole list

lst = [1, 2, 3, 4]
print(lst)

lst.clear()
#This deletes all the elements from the list
print(lst)