import mysql.connector as mq
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import pandas as pd

con = mq.connect(host='localhost', database='emp_db', user='root', password='sunrise.123')

def analyse():
    q = 'Select * from emp_table'
    df = pd.read_sql(q, con)
    return df

def show_chart(df, option):
    window = tk.Tk()
    window.title("Data Analysis")
    window.geometry('805x450+388+154')
    if option == 'Employee Performance Analysis on the basis of Department':
        figure = plt.Figure(figsize=(10, 10), dpi=100)
        ax = figure.add_subplot(221)
        chart_type = FigureCanvasTkAgg(figure, window)
        chart_type.get_tk_widget().pack()
        gdf = df[['EmpDepartment', 'PerformanceRating']].groupby('EmpDepartment').sum()
        gdf.plot(kind='bar', legend=True, ax=ax)

    elif option == 'Job Involvement Analysis on the basis of Department':
        figure = plt.Figure(figsize=(30, 20), dpi=80)
        ax = figure.add_subplot(221)
        chart_type = FigureCanvasTkAgg(figure, window)
        chart_type.get_tk_widget().pack()
        gdf = df[['EmpDepartment', 'EmpJobInvolvement']].groupby('EmpDepartment').sum()
        gdf.plot(kind='bar', legend=True, ax=ax)

    elif option == 'Job Satisfaction Analysis on the basis of Department':
        figure = plt.Figure(figsize=(30, 20), dpi=80)
        ax = figure.add_subplot(221)
        chart_type = FigureCanvasTkAgg(figure, window)
        chart_type.get_tk_widget().pack()
        gdf = df[['EmpDepartment', 'EmpJobSatisfaction']].groupby('EmpDepartment').sum()
        gdf.plot(kind='bar', legend=True, ax=ax)

