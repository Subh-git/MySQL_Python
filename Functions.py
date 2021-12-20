'''
@Author: Subhadeep Bhattacharjee
@Date: 2021-12-18 10:00
@Title: This file contains a class and its method to show function use in mysql through python.

'''



import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Functions():
    '''
    This class is mainly for performing function operations.
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
    
    #This class and its functions are for demonstrating some of the various functions in mysql
    #REMEMBER TO RUN BasicCRUDOperation first.


    def count_students(self):
        '''
        Description:
            This function returns the count of students i.e the number of students from the student table.
        '''

        self.db_cur.execute('SELECT COUNT(name) FROM student')
        mycur = self.db_cur.fetchone()
        print(mycur)

    def sum_score(self):
        '''
        Description:
            This function returns the sum of students scores.
        '''

        self.db_cur.execute('SELECT SUM(score) FROM student')
        for i in self.db_cur:
            print("The sum of scores is: ",i[0])

    def avg_score(self):
        '''
        Description:
            This function returns the average of students scores.
        '''

        self.db_cur.execute('SELECT AVG(score) FROM student')
        for i in self.db_cur:
            print("The average score is: ",i[0])

#group by 
    def avg_score_groupby_course(self):
        '''
        Description:
            This function groups by the course and average scores.
        '''
        self.db_cur.execute('''SELECT AVG(student.score), course.course_name FROM student LEFT JOIN course
        course ON student.course_id = course.course_id GROUP BY course.course_name''')
        for i in self.db_cur:
            print("The average score is: ",i[0]," ",i[1])

    
#user defined function

    def metre_to_foot(self):
        '''
        Description: This function is a user defined function that returns the length in feet.
        '''
        try:
            self.db_cur.execute('''CREATE FUNCTION metre_foot(num decimal(9,2))
                                RETURNS DECIMAL(9,2)
                                DETERMINISTIC
                                BEGIN
                                DECLARE FEET DECIMAL(9,2);
                                SET FEET = num * 3.37;
                                RETURN FEET;
                                END''')


        except Exception as e:
            print(e)


    def test_metre_foot(self,num):
        '''
        Description:
            This function is used to test the function by calling it.
        Parameter:
            It takes self and num as the paramter.
        '''
        self.db_cur.execute("SELECT metre_foot({0})".format(num))
        mycur = self.db_cur.fetchone()
        print("{0} metre is {1} in feet".format(num,mycur[0]))



















if __name__ == '__main__':
    func = Functions()
    func.count_students()
    func.sum_score()
    func.avg_score()
    func.avg_score_groupby_course()
    #func.metre_to_foot()
    func.test_metre_foot(20.23)
