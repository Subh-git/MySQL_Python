'''
@Author: Subhadeep Bhattacharjee
@Date: 2021-12-19 11:50
@Title: This file contains a class and its method to show the use of views in mysql through python.

'''


import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Views():
    '''
    This class is mainly for creating and deleting views.
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
    
    #This class and its functions are for demonstrating views in mysql
    #REMEMBER TO RUN BasicCRUDOperation first.

    def create_view(self):
        '''
        Description:
            This function is used to create views.
        '''
        try:
            self.db_cur.execute(''' CREATE VIEW student_details AS
                        SELECT student.id, student.name, student.course_id, student.score, course.course_name
                        FROM student LEFT JOIN course ON student.course_id = course.course_id
                        UNION ALL 
                        SELECT student.id, student.name, student.course_id, student.score, course.course_name 
                        FROM student RIGHT JOIN course ON student.course_id = course.course_id''')

            self.db_cur.execute('''CREATE VIEW student_score AS 
                                SELECT student.name,student.score FROM student''')
        
            print("View created successfully")
        except Exception as e:
            print(e)


    def display_from_view(self):
        '''
        Description:
            This function is used to display the view as table.
        '''
        try:
            self.db_cur.execute("SELECT * FROM student_details")
            print('(id, name, course_id, score, course_name)')
            for i in self.db_cur:
                print(i)
            
            print("")
            self.db_cur.execute("Select * from student_score")
            for i in self.db_cur:
                print(i)

        except Exception as e:
            print(e)

    def drop_view(self):
        '''
        Description:
            This function is used to delete a view.
        '''
        try:
            self.db_cur.execute("DROP VIEW student_details")
            print("View dropped succesfully")
        except Exception as e:
            print(e)

    def alter_view(self):
        '''
        Description:
            This is used to alter the view.
        '''
        try:
            self.db_cur.execute('''ALTER VIEW student_score AS 
                                SELECT student.name,student.score, student.id FROM student''')
            
            print("View altered succusfully")

        except Exception as e:
            print(e)










if __name__ == '__main__':
    view = Views()
    view.create_view()
    view.display_from_view()
    view.drop_view()
    view.alter_view()
    view.display_from_view()
