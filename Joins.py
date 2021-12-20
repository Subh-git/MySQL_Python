'''
@Author: Subhadeep Bhattacharjee
@Date: 2021-12-18 16:00
@Title: This file contains a class and its method to show various types of join querry in mysql through python.

'''

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Joins():
    '''
    This class is mainly for performing join operations.
    '''
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


    

    #doing the various join operations. REMEBER TO RUN BasicCRUDOp first.

    def Join(self):
        '''
        Description:
            This is the simple join that works as the inner join. It returns the matching columns from two tables as specified.
        '''

        self.db_cur.execute('''SELECT student.id, student.name, student.course_id, course.course_name FROM student
                            JOIN course ON student.course_id = course.course_id ''')
        
        mycur = self.db_cur.fetchall()
        
        print('(id, name, course_id, course_name)')
        for i in mycur:
            print(i)

    def Inner_join(self):
        '''
        Description:
            This is an inner join that should work similar to normal join.
        '''
        self.db_cur.execute('''SELECT student.id, student.name, student.course_id, course.course_name FROM student
                            JOIN course ON student.course_id = course.course_id ''')
        
        print('(id, name, course_id, course_name)')
        for i in self.db_cur:
            print(i)

    def Left_join(self):
        '''
        Decsription:
            Returns all records from the left table, and the matched records from the right table.
        '''
        self.db_cur.execute('''SELECT student.id, student.name, student.course_id, course.course_name FROM student
                            LEFT JOIN course ON student.course_id = course.course_id ''')

        print('(id, name, course_id, course_name)')
        for i in self.db_cur:
            print(i)

    def Right_join(self):
        '''
        Description:
            Returns all records from the right table, and the matched records from the left table.
        '''
        self.db_cur.execute('''SELECT student.id, student.name, student.course_id, course.course_name FROM student
                            RIGHT JOIN course ON student.course_id = course.course_id ''')

        print('(id, name, course_id, course_name)')
        for i in self.db_cur:
            print(i)

    def Full_outer_join(self):
        '''
        Description:
            Returns all records from both tables.
        '''
        self.db_cur.execute(''' SELECT student.id, student.name, student.course_id, student.score, course.course_name
                        FROM student LEFT JOIN course ON student.course_id = course.course_id
                        UNION ALL 
                        SELECT student.id, student.name, student.course_id, student.score, course.course_name 
                        FROM student RIGHT JOIN course ON student.course_id = course.course_id''')

        print('(id, name, course_id, score, course_name)')
        for i in self.db_cur:
            print(i)
        






if __name__ == '__main__':
    join = Joins()
    join.Join()
    print('\n Inner join--------------')
    join.Inner_join()
    print("\n Left join---------------")
    join.Left_join()
    print("\n Right join---------------")
    join.Right_join()
    print("\n Full outer join----------")
    join.Full_outer_join()

