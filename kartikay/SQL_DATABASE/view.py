from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database
import update

class view:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("700x600")
        self.root.title("View Form")
        
        self.table = ttk.Treeview(self.root, columns=['a', 'b', 'c', 'd', 'e', 'f'], show="headings")
        self.table.heading('#1', text='id')
        self.table.heading('#2', text="name")
        self.table.heading('#3', text="mail")
        self.table.heading('#4', text="password")
        self.table.heading('#5', text="Edit")
        self.table.heading('#6', text="Delete")
        
        self.table.column('#1', width=50)
        self.table.column('#2', width=100)
        self.table.column('#3', width=150)
        self.table.column('#4', width=100)
        self.table.column('#5', width=80)
        self.table.column('#6', width=80)
        
        self.table.pack()
        data=database.view()
        print(data)
        
        for i in data:
            print(i)      
            self.table.insert("",len(data),text=i[0],values=[i[0],i[1],i[2],i[3],'Edit','Delete' ]) 
           
        self.table.bind('<Double-Button-1>',self.action)
        self.table.pack()
        self.root.mainloop()
        
    def action(self,n):
        print(n)
        tt=self.table.focus()
        col=self.table.identify_column(n.x)
        print("Column is",col) 
        self.row_id=(self.table.item(tt).get('text'),)

        print("Row is",self.row_id)
        if col=="#6":
            messagebox.askyesno("Delete","Are you sure")
            res=database.delete(self.row_id)
            if res:
                messagebox.showinfo("Success","User Deleted Successfully")
                self.root.destroy()
                view()
        #         # window("User")
            else:
                messagebox.showerror("Error","not deleted")
        if col=="#5":
            m=messagebox.askyesno("Edit","Are you sure")  
            if m:
                self.root.destroy()
                update.update(self.row_id)



if __name__ == "__main__":
    view()