import tkinter as tk
from tkinter import ttk
from tkinter import *
import mysql.connector

def show_emp(window, first_option, second_option):
    details_win = tk.Toplevel(window)
    details_win.geometry('850x500+365+132')

    print(first_option, second_option)
    h = Scrollbar(details_win, orient='horizontal')
    h.pack(side=BOTTOM, fill=X)

    v = Scrollbar(details_win)
    v.pack(side=RIGHT, fill=Y)

    t = Text(details_win, width=80, height=50, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)

    first_option="Gender"
    second_option="Male"
    print(first_option, second_option)

    query = " Select EmployeeID, FullName, Gender, Age from emp_table where {} = '{}';".format(first_option, second_option)
    con = mysql.connector.connect(host='localhost', database='emp_db', user='root', password='ab123')
    if con.is_connected():
        print("Connected")
        cursor = con.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        for i in data:
            print(i)

        count = 0
        for i in data:
            string = ''
            for j in i:
                string = "   " + string + str(j) + " "
            t.insert(END, string+'\n')
            count += 1

    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)

    details_win.lift()
def search_analysis():
    window = tk.Tk()
    window.title("Search Employee Information")
    window.geometry('802x420+390+182')
    window.resizable(0, 0)
    window.config(bg='#F4CE82')


    tk.Label(window, text="Choose Category", font=("Helvetica", 16), bg='#F4CE82').place(x=90, y=80, rely=0)
    clicked = tk.StringVar()
    option_clicked = ttk.Combobox(window, width=35, textvariable=clicked, state="readonly")
    option_clicked['values'] = ['Gender', 'EducationBackground', 'EmpDepartment', 'EmpJobRole']  ##### Here the column names will be be shown
    option_clicked.grid(padx=90, pady=130)
    option_clicked.current(0)

    first_option = option_clicked.get()
    print(first_option)

    con = mysql.connector.connect(host='localhost', database='emp_db', user='root', password='ab123')
    if con.is_connected():
        print("Connected")
        cursor = con.cursor()
        query1 = "Select Distinct {} From emp_details".format(first_option)
        cursor.execute(query1)
        data = cursor.fetchall()

        ls = []
        for i in data:
            ls.append(i)

        print("list", ls)

    tk.Label(window, text="Choose sub-category", font=("Helvetica", 16), bg='#F4CE82').place(x=480, y=80, rely=0)
    clicked_sub = tk.StringVar()
    sub_option = ttk.Combobox(window, width=35, textvariable=clicked_sub, state="readonly")
    sub_option['values'] = ['Cyber', 'IT']  ###### Here the unique values from the chosen column will be shown
    sub_option.grid(row=0, column=2, padx=70, pady=0)
    sub_option.current(0)

    tk.Button(window, text="Search for Employees", width=18, font=('Times New Roman', 16),command=lambda: show_emp(window, option_clicked.get(), sub_option.get())).place(x=300, y=220)

    tk.mainloop()

search_analysis()