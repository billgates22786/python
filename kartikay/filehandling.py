#file handling


#read
# with open("abc.txt","r") as f:
#     a=f.read()
#     print(a)


#write  #overwrite
# with open("abc.txt","w") as f:
#     f.write("hello my name is ironman")


# append
# with open("abc.txt","a") as f:
#     f.write("\a hello my name is saktimaan ")
# with open("abc.txt","r") as f:
#     a=f.read()
#     print(a)

#read
with open("marvel.txt","r") as f:
    a=f.read()
    print(a)

#Create new file  
f = open("myfile.txt", "x")    
    