from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import database
import home

class Login:
    def __init__(self):
        self.root = Tk()
        wid = self.root.winfo_screenwidth()
        hig = self.root.winfo_screenheight()
        self.root.geometry(f"{wid}x{hig}")
        self.root.title("Login Into Anime World")
        
        self.img1 = Image.open("bg.jpg")
        self.img1 = self.img1.resize((wid, hig))
        self.img1 = ImageTk.PhotoImage(self.img1)
        self.l = Label(self.root, image=self.img1)
        self.l.place(x=0, y=0)
        
        self.f = Frame(self.root, bg="black", width=700, height=600, cursor="hand2", relief="ridge", borderwidth=5)
        self.f.pack()
        
        self.l1 = Label(self.f, text="Login Form", font=("arial", 20, "bold"), fg="white", bg="black", borderwidth=5)
        self.l1.place(x=200, y=20)
        self.l3 = Label(self.f, text="Email", font=("arial", 15, "bold"), fg="#3be477", bg="black", borderwidth=5)
        self.l3.place(x=120, y=150)
        self.e3 = Entry(self.f, font=("arial", 15), fg="#3be477", bg="white")
        self.e3.place(x=250, y=150)
        self.l4 = Label(self.f, text="Password", font=("arial", 15, "bold"), fg="#3be477", bg="black")
        self.l4.place(x=120, y=200)
        self.e4 = Entry(self.f, font=("arial", 15), fg="#3be477", bg="white", show="*")
        self.e4.place(x=250, y=200)
        self.btn = Button(self.f, text="Submit", font=("arial", 15, "bold"), fg="#3be477", bg="black", command=self.submit)
        self.btn.place(x=250, y=300)
        
        self.root.mainloop()
    
    def submit(self):
        if self.e3.get() == "" or self.e4.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            data = (self.e3.get(), self.e4.get())
            res = database.login(data)
            print(data)
            if res:
                messagebox.showinfo("Info", "Login successful")
                self.root.destroy()
                home.Home()
            else:
                messagebox.showwarning("Warning", "Invalid email or password")

if __name__ == "__main__":
    Login()
