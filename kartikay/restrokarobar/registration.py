import customtkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

class Regis:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("500x500")
        self.root.title("Registration")
        self.root.resizable(False, False)
        self.root.configure(bg="white")
        
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        
        self.label = customtkinter.CTkLabel(master=self.frame, text="Register Here", font=("Roboto", 24))
        self.label.pack(pady=12, padx=10)   

        self.entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Username")
        self.placeholder = self.entry.get()
        self.entry.pack(pady=12, padx=10)   

        self.entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password")
        self.root.mainloop()
        
        
if __name__ == "__main__":
    Regis()