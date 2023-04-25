import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd



def show_emp():
     details_win = tk.Toplevel(root)
     details_win.geometry('850x500+365+132')

     h = Scrollbar(details_win, orient='horizontal')
     h.pack(side=BOTTOM, fill=X)

     v = Scrollbar(details_win)
     v.pack(side=RIGHT, fill=Y)

     t = Text(details_win, width=80, height=50, wrap=NONE, xscrollcommand = h.set, yscrollcommand = v.set)

     for i in range(200):
          t.insert(END, "this is some text jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj\n")

     t.pack(side=TOP, fill=X)
     h.config(command=t.xview)
     v.config(command=t.yview)

     details_win.lift()

def data_analysis():
     window = tk.Toplevel(root)
     window.title("Data Analysis")

def performance_rating():
     window = tk.Toplevel(root)
     window.title("Performance Rating")
     window.geometry('805x450+388+154')

     tk.Label(window, text="Enter Employee ID", font=("Helvetica", 14), bg='#F4CE82').place(x=150, y=60)
     emp_id = tk.Entry(window, font=("Helvetica", 11), width=42).place(x=340, y=60, height=25)

     tk.Label(window, text="Enter Performance Rating (1 to 5)", font=("Helvetica", 14), bg='#F4CE82').place(x=150, y=110)
     emp_rating = tk.Entry(window, font=("Helvetica", 11), width=26).place(x=470, y=110, height=25)

     tk.Label(window, text="Update Performance Ranking for ....", font=("Helvetica", 14), bg='#F4CE82').place(x=150,y=160)

     tk.Button(window, text="Update Rating", width=18, font=('Times New Roman', 16), command=lambda: show_emp(emp_id, emp_rating)).place(x=300, y=240)


def search_analysis():
     window = tk.Toplevel(root)
     window.title("Search Employees / Show Data Analysis")
     window.geometry('802x420+390+182')
     window.resizable(0,0)

     tk.Label(window, text="Choose Category", font=("Helvetica", 16)).place(x=90, y=50, rely=0)
     clicked = tk.StringVar()
     option_clicked = ttk.Combobox(window, width = 35, textvariable = clicked)
     option_clicked['values'] = ('Audit', 'Tax', 'Advisory', 'Consulting')   ##### Here the column names will be be shown
     option_clicked.grid(padx=90, pady=100)
     option_clicked.current(0)

     tk.Label(window, text="Choose sub-category", font=("Helvetica", 16)).place(x=480, y=50, rely=0)
     clicked_sub = tk.StringVar()
     sub_option = ttk.Combobox(window, width = 35, textvariable=clicked_sub)
     sub_option['values'] = ('Cyber', 'IT')    ###### Here the unique values from the chosen column will be shown
     sub_option.grid(row=0, column=2, padx=70, pady=0)
     sub_option.current(0)

     tk.Button(window, text="Search for Employees", width=18, font=('Times New Roman', 16), command=lambda: show_emp()).place(x=300, y=180)

root = tk.Tk()

root.title('Employee Management System')
root.geometry('800x420+390+182')
tk.Label(root, text="Employee Analysis Portal", font=('Helvetica', 18, "underline"), wraplength=400).place(x=260, y=50)

tk.Button(root, text='Enter Performance Ratings', width=20, font=('Times New Roman', 16), command=lambda: performance_rating()).place(x=274, y=140)
tk.Button(root, text='Search Employees', width=20, font=('Times New Roman', 16), command=lambda: search_analysis()).place(x=274, y=210)
tk.Button(root, text='Perform Data Analysis', width=20, font=('Times New Roman', 16), command=lambda: data_analysis()).place(x=274, y=280)
root.update()
root.mainloop()


