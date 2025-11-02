# li=[]
# for i in range(10):
#     li.append(i)
# print(li)

li=[i for i in range(10)]
print(li)

li2=[i+3 for i in range(10)]
print(li2)

li3=[i for i in range(10) if i%2==0]
print(li3)


# li4=[]
# for i in range(10):
#     if i%2==0:
#         li4.append(i)
#     else:
#         li4.append("bye")
# print(li4)

# li4=[i*i if i%2==0 else "bye" for i in range(10)]
# print(li4)

# l5=[i for i in range(5) for j in range(i+1)]
# print(l5)


# for i in range(3):
#     for j in range(5):
#         print(i,end=" ")
    # print()