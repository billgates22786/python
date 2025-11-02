f=open("Main.txt","r+")
fileContent=input("Enter your contents: ")
f.write(fileContent)
g=open("Vowels.txt","r+")
h=open("Consonants.txt","r+")
for i in f:
  if i in "aeiouAEIOU":
    g.write(i)
  else:
    h.write(i)
for i in g:
  print(i)
for i in h:
  print(i)
f.close()
g.close()
h.close()
