from tkinter import *
from tkinter import messagebox

class form:
    def __init__(self):
        self.root=Tk()
        wid=self.root.winfo_screenwidth()
        hig=self.root.winfo_screenheight()
        self.root.geometry(f"{wid}x{hig}")
        self.root.title("Registration Form")
        self.root.config(bg="#f0f0f0")
        self.f=Frame(self.root,bg="white",width=700,height=600,borderwidth=10)
        self.f.pack()
        self.l1 = Label(self.f, text="Registration Form", font=("Arial", 24, "bold"), fg="#333", bg="white")
        self.l1.place(x=200, y=20)
        self.l2 = Label(self.f, text="Name:", font=("Arial", 14), fg="#333", bg="white")
        self.l2.place(x=120, y=100)
        self.e2 = Entry(self.f, font=("Arial", 14), fg="#333", bg="#f5f5f5", width=30)
        self.e2.place(x=250, y=100)
        self.l3 = Label(self.f, text="Email:", font=("Arial", 14), fg="#333", bg="white")
        self.l3.place(x=120, y=150)
        self.e3 = Entry(self.f, font=("Arial", 14), fg="#333", bg="#f5f5f5", width=30)
        self.e3.place(x=250, y=150)
        self.l4 = Label(self.f, text="Password:", font=("Arial", 14), fg="#333", bg="white")
        self.l4.place(x=120, y=200)
        self.e4 = Entry(self.f, font=("Arial", 14), fg="#333", bg="#f5f5f5", show="*", width=30)
        self.e4.place(x=250, y=200)
        self.btn = Button(self.f, text="Submit", font=("Arial", 14, "bold"), fg="white", bg="#007BFF", activebackground="#0056b3", activeforeground="white", cursor="hand2",command=self.submit)
        self.btn.place(x=250, y=300, width=200, height=40)
        self.root.mainloop()
    
    def submit(self):
         if self.e2.get() == "" or self.e3.get() == "" or self.e4.get() == "":
            messagebox.showerror("Error", "You got 404D")
            messagebox.showinfo("Info","shit shit! shit! shit! shit! shit! shit! shit!")
if __name__ == "__main__":
    form()