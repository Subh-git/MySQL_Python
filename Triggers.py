'''
@Author: Subhadeep Bhattacharjee
@Date: 2021-12-20 18:00
@Title: This file contains a class and its method to show the use of triggers in mysql through python.

'''

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Triggers():
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

#Triggers can be mainly of update, delete and insert. and before and after for each of them.

    def create_trigger(self):
        '''
        Description:
            This is used to create a trigger when insert happens.
        '''
        self.db_cur.execute('''CREATE TRIGGER tr_ins_name
            BEFORE INSERT ON student
            FOR EACH ROW
            SET NEW.name = UPPER(NEW.name);''')
        
        print("Trigger created succesfully")

        self.db_cur.execute('''INSERT INTO student VALUES(15,"katie",3,84),(16,"jack",2,52) ''')
        self.db_cur.execute("SELECT * FROM student")
        for i in self.db_cur:
            print(i)

    def drop_trigger(self):
        '''
        Description:
            This is used to drop the trigger if exist.
        '''
        self.db_cur.execute("DROP TRIGGER IF EXISTS tr_ins_name")
        
        print("Trigger dropped succesfully")
    


if __name__ == '__main__':
    tr = Triggers()
    tr.create_trigger()
    tr.drop_trigger()