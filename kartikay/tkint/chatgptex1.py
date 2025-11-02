# from tkinter import Tk, Button, Entry

# class Calculator:
#     def __init__(self):
#         self.root = Tk()
#         self.root.title("Simple Calculator")
#         self.root.geometry("400x400")

#         self.entry = Entry(self.root, width=40, borderwidth=5)
#         self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#         self.create_buttons()
#         self.root.mainloop()

#     def create_buttons(self):
#         buttons = [
#             '7', '8', '9', '/', '4', '5', '6', '*',
#             '1', '2', '3', '-', '0', '.', '=', '+'
#         ]
#         row_val = 1
#         col_val = 0
#         for button in buttons:
#             command = lambda x=button: self.on_button_click(x)
#             Button(self.root, text=button, padx=20, pady=20, command=command).grid(row=row_val, column=col_val)
#             col_val += 1
#             if col_val > 3:
#                 col_val = 0
#                 row_val += 1

#     def on_button_click(self, char):
#         if char == '=':
#             try:
#                 result = str(eval(self.entry.get()))
#                 self.entry.delete(0, 'end')
#                 self.entry.insert(0, result)
#             except Exception as e:
#                 self.entry.delete(0, 'end')
#                 self.entry.insert(0, "Error")
#         else:
#             current_text = self.entry.get()
#             self.entry.delete(0, 'end')
#             self.entry.insert(0, current_text + char)

# if __name__ == "__main__":
#     Calculator()
#********************************************************************************************************************************
# from tkinter import Tk, Button, Entry, Frame

# class Calculator:
#     def __init__(self):
#         self.root = Tk()
#         self.root.title("Simple Calculator")
#         self.root.geometry("400x400")
#         self.root.configure(bg='lightgray')

#         self.entry = Entry(self.root, width=40, borderwidth=5, font=('Arial', 18))
#         self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#         self.create_buttons()
#         self.root.mainloop()

#     def create_buttons(self):
#         buttons = [
#             '7', '8', '9', '/', '4', '5', '6', '*',
#             '1', '2', '3', '-', '0', '.', '=', '+'
#         ]

#         button_frame = Frame(self.root, bg='lightgray')
#         button_frame.grid(row=1, column=0, columnspan=4)

#         row_val = 0
#         col_val = 0
#         for button in buttons:
#             command = lambda x=button: self.on_button_click(x)
#             Button(button_frame, text=button, padx=20, pady=20, command=command, font=('Arial', 14),
#                    bg='white', fg='black', activebackground='lightblue', borderwidth=2).grid(row=row_val, column=col_val, padx=5, pady=5)
#             col_val += 1
#             if col_val > 3:
#                 col_val = 0
#                 row_val += 1

#     def on_button_click(self, char):
#         if char == '=':
#             try:
#                 result = str(eval(self.entry.get()))
#                 self.entry.delete(0, 'end')
#                 self.entry.insert(0, result)
#             except Exception as e:
#                 self.entry.delete(0, 'end')
#                 self.entry.insert(0, "Error")
#         else:
#             current_text = self.entry.get()
#             self.entry.delete(0, 'end')
#             self.entry.insert(0, current_text + char)

# if __name__ == "__main__":
#     Calculator()
#**********************************************************************************************************************************
from tkinter import Tk, Button, Entry, Frame

class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.title("Apple-Style Calculator")
        self.root.geometry("350x500")
        self.root.configure(bg='black')

        self.entry = Entry(self.root, width=16, borderwidth=0, font=('Helvetica', 24), bg='black', fg='white', insertbackground='white')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()
        self.root.mainloop()

    def create_buttons(self):
        buttons = [
            ('7', 'black'), ('8', 'black'), ('9', 'black'), ('/', 'orange'),
            ('4', 'black'), ('5', 'black'), ('6', 'black'), ('*', 'orange'),
            ('1', 'black'), ('2', 'black'), ('3', 'black'), ('-', 'orange'),
            ('0', 'black'), ('.', 'black'), ('=', 'orange'), ('+', 'orange')
        ]

        button_frame = Frame(self.root, bg='black')
        button_frame.grid(row=1, column=0, columnspan=4)

        row_val = 0
        col_val = 0
        for (btn_text, color) in buttons:
            command = lambda x=btn_text: self.on_button_click(x)
            Button(button_frame, text=btn_text, padx=20, pady=20, command=command,
                   font=('Helvetica', 18), bg=color, fg='white', activebackground='gray30', borderwidth=0).grid(row=row_val, column=col_val, padx=5, pady=5, ipadx=10, ipady=10)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, 'end')
                self.entry.insert(0, result)
            except Exception as e:
                self.entry.delete(0, 'end')
                self.entry.insert(0, "Error")
        else:
            current_text = self.entry.get()
            self.entry.delete(0, 'end')
            self.entry.insert(0, current_text + char)

if __name__ == "__main__":
    Calculator()
