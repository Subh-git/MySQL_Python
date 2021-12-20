'''
@Author: Subhadeep Bhattacharjee
@Date: 2021-12-20 21:00
@Title: This file contains a class and its method to show the use of transaction control in mysql through python.

'''

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Transaction():
 
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

    
    def create_transaction(self):
        '''
        Description:
            This function is used to mimick the transaction control query in mysql. 
        '''

        self.db_cur.execute("drop table if exists wage")
        self.db_cur.execute('''create table wage(
        emp_id int primary key,
        name varchar(15),
        wage int
        )''')

        self.db_cur.execute("insert into wage values(1,'Joseph', 15000), (2,'David', 20000), (3, 'Rahul', 25000)")
        self.mydb.commit()
        print("To print the wage table: ")
        print('\n emp_id, name, wage ')
        self.db_cur.execute("select * from wage")
        for i in self.db_cur:
            print(i)


        #create a transaction where we commit and rollback few changes.
        self.db_cur.execute("start transaction")
        self.db_cur.execute("select @max:= MAX(wage) from wage")
        mycur = self.db_cur.fetchone()
        print(mycur)
        print("Inserting value before savepoint")
        self.db_cur.execute("insert into wage values(4,'Harold', 18000), (5,'Joshua', 10000)")
        self.db_cur.execute("savepoint my_savepoint")
        print("Inserting after custom created savepoint: ")
        self.db_cur.execute("insert into wage values(6,'Lee', 8000), (7,'Ginny', 9000)")
        self.db_cur.execute("rollback to savepoint my_savepoint")
        self.db_cur.execute("insert into wage values(8,'Subh', 14000), (9,'Shyam', 26000)")
        self.mydb.commit()

        self.db_cur.execute("select * from wage")
        print('\n emp_id, name, wage ')
        for i in self.db_cur:
            print(i)






    

if __name__ == '__main__':
    ob = Transaction()
    ob.create_transaction()