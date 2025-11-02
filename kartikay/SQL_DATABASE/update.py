from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import database
import view
class update:
    def __init__(self,id):
        self.root = Tk()
        wid=self.root.winfo_screenwidth()
        hig=self.root.winfo_screenheight()
        self.root.geometry(f"{wid}x{hig}")
        self.root.title("update data")
        self.id=id
        print(self.id)
        res=database.getone(self.id)
        print(res)

        # print("----------------",self.id[0])

        self.img1=Image.open("bg.jpg")
        self.img1=self.img1.resize((wid,hig))
        self.img1=ImageTk.PhotoImage(self.img1)
        self.l=Label(self.root,image=self.img1)
        self.l.place(x=0,y=0)
        self.f=Frame(self.root,bg="lightblue",width=700,height=600,cursor="hand2",relief="ridge",borderwidth=5)
        self.f.pack()
        self.l1=Label(self.f,text="Registration Form",font=("arial",20,"bold"),fg="red",bg="#dbe5e6",borderwidth=5)
        self.l1.place(x=200,y=20)
        self.l2=Label(self.f,text="Name",font=("arial",15,"bold"),fg="red",bg="lightblue",borderwidth=5)
        self.l2.place(x=120,y=100)
        self.e2=Entry(self.f,font=("arial",15) ,fg="red", bg="lightblue")
        self.e2.place(x=250,y=100)
        self.l3=Label(self.f,text="email",font=("arial",15,"bold"),fg="red",bg="lightblue",borderwidth=5)
        self.l3.place(x=120,y=150)
        self.e3=Entry(self.f,font=("arial",15) ,fg="red", bg="lightblue")
        self.e3.place(x=250,y=150)
        self.l4=Label(self.f,text="password",font=("arial",15,"bold"),fg="red",bg="lightblue")
        self.l4.place(x=120,y=200)
        self.e4=Entry(self.f,font=("arial",15) ,fg="red", bg="lightblue",show="*")
        self.e4.place(x=250,y=200)
        self.btn=Button(self.f,text="Submit",font=("arial",15,"bold"),fg="red",bg="lightblue",command=self.submit)
        self.btn.place(x=250,y=300)

        self.root.mainloop()

    def submit(self):
        if self.e2.get()=="" or self.e3.get()=="" or self.e4.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            data=(self.e2.get(),self.e3.get(),self.e4.get(),self.id[0])
            res=database.update(data)
            print(data)
            if res:
                messagebox.showinfo("info","data inserted")
                self.root.destroy()
                view.view()
            else:
                messagebox.showwarning("warning","data not inserted")

if __name__ == "__main__":
    update()