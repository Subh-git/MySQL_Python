'''
@Author: Subhadeep Bhattacharjee
@Date: 2021-12-20 20:00
@Title: This file contains a class and its method to show the use of noramlisation in mysql through python.

'''


import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Normalisation():

    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password= os.getenv("MySQL_Password"),
                database = 'college',
                auth_plugin='mysql_native_password'
                )
    
            self.db_cur = self.mydb.cursor()
        except Exception as e:
            print(e)
            exit()

    def first_normal_form(self):
        '''
        Description:
            This function tells us about the first normal form which is related to reducing data redundancy and atomicty 
            principle.
        '''
        self.db_cur.execute('''CREATE TABLE details (
                student_name varchar(15),
                age int,
                department varchar(25)
        )''')

        self.db_cur.execute('''insert into details values('Ron', 15, 'Physics, Maths'),('Jhon',12, 'English,Maths')''')
        print("student name, age, department")
        self.mydb.commit()
        self.db_cur.execute("Select * from details")
        for i in self.db_cur:
            print(i)


        print("This table should be changed to following")
        self.db_cur.execute("DELETE FROM details")
        self.db_cur.execute('''insert into details values('Ron', 15, 'Physics'),('Ron',15,'Maths'),
        ('Jhon',12, 'English'),('Jhon',12, 'Maths')''')
        self.mydb.commit()
        print("\n After changing it to 1NF")
        self.db_cur.execute("Select * from details")
        print("student name, age, department")
        for i in self.db_cur:
            print(i)

    def drop_details(self):
        '''
        Description:
            This is used to drop the table details.
        '''
        self.db_cur.execute("drop table if exists details")
        print("Dropped successfully")




if __name__ == '__main__':
    norm = Normalisation()
    norm.first_normal_form()
    norm.drop_details()