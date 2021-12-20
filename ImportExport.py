'''
@Author: Subhadeep Bhattacharjee
@Date: 2021-12-20 15:00
@Title: This file contains a class and its method to import and export databases in mysql through python.

'''

import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()

class ImportExport():
    '''
    This class is mainly for importing and exporting databases.
    '''
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password= os.getenv("MySQL_Password"),
                database = 'Employee',
                auth_plugin='mysql_native_password'
                )
    
            self.db_cur = self.mydb.cursor()
        except Exception as e:
            print(e)
            exit()


    def export(self):
        '''
        Description:
            This function is used to export the data to a different database/place.
        '''
        try:
            os.system('mysqldump -u root -p Employee > Employee_backup.sql')
            print("Exported")
           
        except Exception as e:
            print(e)

    def import_db(self):
        '''
        Description:
            This function is used to import the data from some location/database to our desired database.
        '''
        try:
            self.db_cur.execute("CREATE DATABASE Employee_import")
            os.system('mysql -u root -p Employee_import < Employee_backup.sql')
            print("Imported")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    imex = ImportExport()
    imex.export()
    imex.import_db()
   
    
