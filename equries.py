import analysis as anal
import mysql.connector as mq

class Choice:

    ch=0
    def __init__(self):
        self.ch = int(input('Enter choice:'))
        return self.ch

class Queries(Choice):
    con = mq.connect(host='localhost', database='emp_db', user='root', password='sunrise.123')
    x = 0
    def __init__(self):
        self.x= super(Queries,self).__init__()
        if self.x==1:
            self.dfetch()
        elif self.x==2:
            self.prate()
        elif self.x==3:
          anal.Analyse()

    def dfetch(self):
        cursor = self.con.cursor()
        dname = input('Enter name of department: ')
        q = "Select FullName from emp_db.emp_table WHERE EmpDepartment= %s"
        cursor.execute(q,(dname,))
        res = cursor.fetchall()
        for i in res:
            print(i)


    def prate(self):
        cursor = self.con.cursor()
        e_id=input('Enter the employee ID to update performance rating: ')
        rate=int(input('Enter the New Employee Performance Rating: '))
        q="Update emp_table set PerformanceRating=%s where EmployeeID= %s"
        cursor.execute(q,(rate,e_id,))
        self.con.commit()
        print("Record Updated successfully ")

