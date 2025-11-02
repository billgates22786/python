from tkinter import *

class regis:
    def __init__(self):
        self.r = Tk()
        self.r.geometry("700x600")
        # self.r.resizable(False,False)
        self.r.title("Registration Form")
        self.l1=Label(self.r,text="Registration Form",font=("arial",20,"bold"),fg="red",bg="#dbe5e6",borderwidth=5)
        self.l1.place(x=200,y=20)
        self.l2=Label(self.r,text="Name",font=("arial",15,"bold"),fg="red",bg="lightblue",borderwidth=5)
        self.l2.place(x=120,y=100)
        self.e2=Entry(self.r,font=("arial",15) ,fg="red", bg="lightblue")
        self.e2.place(x=250,y=100)
        self.l3=Label(self.r,text="email",font=("arial",15,"bold"),fg="red",bg="lightblue",borderwidth=5)
        self.l3.place(x=120,y=150)
        self.e3=Entry(self.r,font=("arial",15) ,fg="red", bg="lightblue")
        self.e3.place(x=250,y=150)
        self.l4=Label(self.r,text="password",font=("arial",15,"bold"),fg="red",bg="lightblue")
        self.l4.place(x=120,y=200)
        self.e4=Entry(self.r,font=("arial",15) ,fg="red", bg="lightblue",show="*")
        self.e4.place(x=250,y=200)
        self.values=["male","female"]
        for i in range(len(self.values)):
            # print(self.values[i])
            self.e5=Radiobutton(self.r,font=("arial",15) ,fg="red", bg="lightblue",text=self.values[i])
            if i==0:
                self.e5.place(x=250,y=250)
            else:
                self.e5.place(x=350,y=250)

        self.e6=Checkbutton(self.r,font=("arial",15) ,text="remember me",fg="red", bg="lightblue")
        self.e6.place(x=250,y=300)
        self.btn=Button(self.r,font=("arial",15) ,text="Submit",fg="red", bg="lightblue",command=self.submit)
        self.btn.place(x=250,y=350)
        self.r.mainloop()

    def submit(self):
        print(self.e2.get())
        print(self.e3.get())
        print(self.e4.get())
        print(self.e6.get())

# obj = regis()
if __name__ == "__main__":
    obj = regis()
    

