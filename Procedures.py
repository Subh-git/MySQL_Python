'''
@Author: Subhadeep Bhattacharjee
@Date: 2021-12-20 12:00
@Title: This file contains a class and its method to show the use of Procedures in mysql through python.

'''
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Procedures():
    '''
    This class is mainly for creating and deleting procedures.
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

#REMEMBER TO RUN BasicCRUDOperation first.

    def create_procedure_without_paramter(self):
        '''
        Description:
            This function is used to create a proceure that doesn't take parameter.
        '''
        try:
            self.db_cur.execute('''CREATE PROCEDURE display_names()
                                    BEGIN
                                    SELECT name FROM student;
                                    END
                                    ''')
            print("display_names procedure created succesfully")

        
        except Exception as e:
            print(e)



    def procedure_with_in(self):
        '''
        Description:
            This is used to create a procedure with in type parameter. i.e it takes an argument.
        
        '''
        try:
            self.db_cur.execute('''CREATE PROCEDURE get_students(IN lim INT)
                                    BEGIN
                                    SELECT * FROM student LIMIT lim;
                                    SELECT COUNT(id) AS 'Total_students' FROM student;
                                    END
                                    ''')
            print("get student procedure created succesfully")

        
        except Exception as e:
            print(e)



    def procedure_with_out(self):
        '''
        Description:
            This procedure is used to get the highest marks as output variable.
        '''
        try:
            self.db_cur.execute('''CREATE PROCEDURE get_highest(OUT high INT)
                                    BEGIN
                                    SELECT MAX(score) INTO high FROM student;
                                    END
                                    ''')
            print("get_highest procedure created succesfully")

        
        except Exception as e:
            print(e)





    def drop_procedure_ifexist(self):
        '''
        Description:
            This is used to drop a procedure if it exist.
        '''
        self.db_cur.execute("DROP PROCEDURE IF EXISTS display_names")
        self.db_cur.execute("DROP PROCEDURE IF EXISTS get_students")
        self.db_cur.execute("DROP PROCEDURE IF EXISTS get_highest")
        print("Procedure deleted succesfully")



    def call_procedures(self):
        '''
        Description:
            This function is used to call procedures.
        '''
        print("Calling display_names procedure")
        
        self.db_cur.callproc('display_names')
        for i in self.db_cur.stored_results():
            print(i.fetchall())

        #self.db_cur.execute("CALL display_names()")  this returns the error as multi=true 

        print("\n calling get_student procedure")
        self.db_cur.callproc('get_students',[2,])
        for result in self.db_cur.stored_results():
            rlist = result.fetchall()
            for row in rlist:
                print(row)


        print("\n calling get_highest procedure")
        self.db_cur.execute("CALL get_highest(@M)")
        self.db_cur.execute("SELECT @M")
        for i in self.db_cur:
            print(i[0])


   









if __name__ == '__main__':
    proc = Procedures()
    proc.create_procedure_without_paramter()
    proc.procedure_with_in()
    proc.procedure_with_out()
    proc.call_procedures()
    proc.drop_procedure_ifexist()