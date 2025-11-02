#Q1 Create a list of 10 number and print the list
list=[1,2,3,4,5,6,7,8,9,10]


#Q2 Create a list [1,10,100,["hello",22,[10000,99999,True],2],3,6,8] and add 59 on 3 location after that append 5 and print list and length of list add 3.14 before true
li=[1,10,100,["hello",22,[10000,99999,True],2],3,6,8]
li.insert(3,"59")
print(li)
li.append(5)
print(li)
print("Lenght of the List",len(li))
li[4][2].insert(2, 3.14)
print(li)


#Q3  create a list of 10 elements and print all elements are even locations
# Example:
#     x = [1,4,2,42,4,6,2,56,4,56,2]
#     Result is: 1 2 4 6 56 56


x = [1,4,2,42,4,6,2,56,4,56,2]
print(x[0::2])


#Q4 create a list with values ["Gaurav",12,23,33.33,"Sharma",True] and print only elements which are string
St=["Gaurav",12,23,33.33,"Sharma",True]
for i in St:
    if isinstance(i, str):
        print("ONLY STRING: ",i)


#Q5 add all the number present in above list
x=[1,2,3,4,5,6,7,8,9,10]
total = 0
for i in x:
    total +=i

print("TOTAL OF THE STRING IS:",total)


# Q6 Create a list with 5 friends and ask user a friend name and
# add that name in the friend list,
# and print the list
# after that ask user to most important friend and add that friend
# at user choice

# Ex: [1,2,3,4,5]
# -> Enter anothe fiend: Raju
# [1,2,3,4,5,"Raju"]
# --> Most import afiedn: Billa
# --> Please location for billa: 1
# [1,"Billa",3,4,5,"Raju"]

fg=[1,2,3,4,5,6]
f=input("Enter Friend name:")
g=input("Most important friend name:")
k=int(input("Enter the index number for the placement of the important friend name:"))
fg.append(f)
print(fg)
fg.insert(k,g)
print("final freind list",fg)

    





