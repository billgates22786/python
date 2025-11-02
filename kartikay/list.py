# # list -[] ,hetrogenous,mutable,ordered,indexed,allow duplicates

# # li=[1,3,5,"hello",True,2.33]
#    #0 1  2    3    4    5
    
# # print(li)
# # print(len(li))
# # print(li[0])
# # print(li[3])
# # print(li[-1])
# # print(li[-3])
# # print(li[3],li[2])
# # print(li[3][2])

# #slicing  start : stop : step
# # print(li[0:4])
# # print(li[0:5:2])
# # print(li[4:0:-1])
# # print(li[4:0:-2])
# # print(li[::2])
# # print(li[::-1])
# # print(li[2:])

#   #0 1  2    3 0  1   2    3     4  0  1  2  5        4
# a=[3,5,"bye",[22,44,True,"hello",["hi",66,0],999],25.333,5,0]


# a.insert(3,"Kartikay")
# # print(a[3])
# # print(a[3][2])
# # print(a[3][4][1])

# a.append("hello")
# print(a)


# print(a)

# a.remove("hi")
# print(a)

# a.pop(0)
# print(a)

# a.extend([1,2,34,4])
# print(a)

# print(a.count(5))
# print(a.index(5))


# a.reverse()
# print(a)

# # a.clear()
# # print(a)

# del(a)
# print(a)


# x=[1,2,3,4,5,44,50,22,3]
# x.sort(reverse=True)
# print(x)

# for i in x:
    # print(i)
    # if i%2==0:
    #     print(i)



# x=[1,2,3,4,5,"hello",44,50,22,3]
# for i in x:
#     print(i,end=" ")
    # if isinstance(i,int):
    #     print(i)
    # if type(i)==int:
    #     print(i,end=" ")


a=int(input("enter a number "))
li=[]
for i in range(a):
        b=input(f"Enter {i+1} Number: ") 
        li.append(b)
        # if isinstance(i,int):
            #   li.append(b) 
                 
li2=[]
for i in li:
        if i.isdigit():
            li2.append(int(i))
print(li2)