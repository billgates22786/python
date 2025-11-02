from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import view
import database

class home:
    def __init__(self,res):
        self.root = Tk()
        wid = self.root.winfo_screenwidth()
        hig = self.root.winfo_screenheight()
        self.root.geometry(f"{wid}x{hig}")
        self.root.title("Home Page")
        
        self.img1 = Image.open("bg.jpg")
        self.img1 = self.img1.resize((wid, hig))
        self.img1 = ImageTk.PhotoImage(self.img1)
        self.l = Label(self.root, image=self.img1)
        self.l.place(x=0, y=0)
       
        self.l1 = Label(self.root, text="Home Page", font=("arial", 30, "bold"), fg="white", bg="#f33221", borderwidth=5)
        self.l1.place(x=(wid - self.l1.winfo_reqwidth()) // 2, y=0)
        
        self.f = Frame(self.root, bg="black", width=700, height=600, cursor="hand2", relief="ridge", borderwidth=5)
        self.f.pack()
        
        self.l2 = Label(self.f, text="Welcome to Anime World", font=("arial", 20, "bold"), fg="white", bg="black", borderwidth=5)
        self.l2.place(x=200, y=20)
        res = res[0][1]  # Adjusting the result display
        self.l3 = Label(self.root, text=res, font=("arial", 15, "bold"), fg="white", bg="black", borderwidth=5)
        self.l3.pack()
        self.btn = Button(self.f, text="Submit", font=("arial", 15, "bold"), fg="#3be477", bg="black", command=self.submits)
        self.btn.place(x=250, y=300)

        self.root.mainloop()

    def submits(self):
        messagebox.askyesno("Attention", "Home Destroyed")
        self.root.destroy()
        view.view()

if __name__ == "__main__":
    home()