from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

class Home:
    def __init__(self):
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
        label_width = self.l1.winfo_reqwidth()
        label_height = self.l1.winfo_reqheight()
        self.l1.place(x=(wid - label_width) // 2, y=0)
        
        self.root.mainloop()

if __name__ == "__main__":
    Home()
