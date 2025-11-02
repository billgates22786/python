from tkinter import *
from tkinter import messagebox
import random as rn

class dice:
    def __init__(self):
        self.root = Tk()
        self.root.title("Dice Game")
        wid = self.root.winfo_screenwidth()
        hig = self.root.winfo_screenheight()
        self.root.geometry(f"{wid}x{hig}")
        self.root.config(bg="#f0f0f0")
        self.frame = Frame(self.root, bg="white", width=700, height=600, borderwidth=10)
        self.frame.pack()
        self.l1 = Label(self.frame, text="Dice Game", font=("Arial", 24, "bold"), fg="#333", bg="white")
        self.l1.place(x=200, y=20)
        self.l2 = Label(self.frame, text="User 1:", font=("Arial", 14), fg="#333", bg="white")
        self.l2.place(x=120, y=100)
        self.user1_input = Entry(self.frame, font=("Arial", 14), width=5)
        self.user1_input.place(x=200, y=100)
        self.l3 = Label(self.frame, text="User 2:", font=("Arial", 14), fg="#333", bg="white")
        self.l3.place(x=120, y=150)
        self.user2_input = Entry(self.frame, font=("Arial", 14), width=5)
        self.user2_input.place(x=200, y=150)
        self.l4 = Label(self.frame, text="User 3:", font=("Arial", 14), fg="#333", bg="white")
        self.l4.place(x=120, y=200)
        self.user3_input = Entry(self.frame, font=("Arial", 14), width=5)
        self.user3_input.place(x=200, y=200)
        self.l5 = Label(self.frame, text="User 4:", font=("Arial", 14), fg="#333", bg="white")
        self.l5.place(x=120, y=250)
        self.user4_input = Entry(self.frame, font=("Arial", 14), width=5)
        self.user4_input.place(x=200, y=250)
        self.roll_button = Button(self.frame, text="Roll Dice", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.roll_dice)
        self.roll_button.place(x=200, y=300)
        self.root.mainloop()
        
    def roll_dice(self):
        try:
            user1 = int(self.user1_input.get())
            user2 = int(self.user2_input.get())
            user3 = int(self.user3_input.get())
            user4 = int(self.user4_input.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for all users!")
            return
        
        if not(1 <= user1 <= 6) or not(1 <= user2 <= 6) or not(1 <= user3 <= 6) or not(1 <= user4 <= 6):
            messagebox.showerror("Input Error", "Numbers must be between 1 and 6!")
            return
        
        computer_roll = rn.randint(1, 6)
        messagebox.showinfo("Computer Roll", f"Computer rolled: {computer_roll}")

        if user1 == computer_roll:
            winner = "User 1"
        elif user2 == computer_roll:
            winner = "User 2"
        elif user3 == computer_roll:
            winner = "User 3"
        elif user4 == computer_roll:
            winner = "User 4"
        else:
            winner = "No one"
        
        messagebox.showinfo("Result", f"{winner} wins!")
        
if __name__ == "__main__":
    dice()
