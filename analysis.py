import mysql.connector as mq
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
class Analyse:
    con = mq.connect(host='localhost', database='emp_db', user='root', password='sunrise.123')
    def __init__(self):
        q = 'Select * from emp_table'
        df = pd.read_sql(q,self.con)


        plt.pie(df.groupby(['PerformanceRating']).size(), labels=df.groupby(['PerformanceRating']).size())
        plt.show()
       # print(df.groupby(['EmpJobRole']).sum().plot(kind='pie', y='PerformanceRating'))
