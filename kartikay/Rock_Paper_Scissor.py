#Create a rock paper Scissors game
import random as rn
User_wins=0
Computer_wins=0
draws=0
k=int(input("How many rounds you want to play:"))
for i in range(k):
    c=rn.choice(["rock","paper","scissors"])
    print("Enter your choice:\n1.rock\n2.paper\n3.scissor")
    u=input("Enter your choice:")
    print("Choice Selected by Computer:",c)
    print("Choice Selected by User:",u)
    if c==u:
        print("Draw")
        draws +=1
    elif (c=="rock" and u=="paper") or (c=="paper" and u=="scissors") or (c=="scissors" and u=="rock"):
        print("User win")
        User_wins +=1
    elif c=="rock" and u=="scissors" or c=="paper" and u=="rock" or c=="scissors" and u=="paper":
        print("Computer win") 
        Computer_wins +=1
    else:
        print("Invalid Choice")    
        
        
print("\nFinal Scores:")
print("User Wins:", User_wins)
print("Computer Wins:", Computer_wins)
print("Draws:", draws)        
print("My name is devilman c")