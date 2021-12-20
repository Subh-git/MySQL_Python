'''
@Author: Subhadeep Bhattacharjee
@Date: 2021-12-19 20:00
@Title: This file contains a class and its method to show index creation and deletion in mysql through python.

'''


import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Indexes():
    '''
    This class is mainly for creating and deleting indexes.
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
    
    #This class and its functions are for demonstrating indexes in mysql
    #REMEMBER TO RUN BasicCRUDOperation first.

    def create_index(self):
        '''
        Description:
            This method is usedd to create an index.
        '''
        try:

            self.db_cur.execute("""CREATE INDEX student_id_idx 
                                    ON student(id)""")
            
            self.db_cur.execute("""CREATE INDEX student_name_idx 
                                    ON student(name)""")
                        
            print("Index on student id created successfully")

        except Exception as e:
            print(e)


    def show_indexes(self):
        '''
        Desscription:
            Thisfunction is used to show created indexes.
        '''

        try:
            self.db_cur.execute("SHOW INDEX FROM student")
            for i in self.db_cur:
                print(i[2])

        except Exception as e:
            print(e)

    def drop_index(self):
        '''
        Description:
            This function is used to delete an index.
        '''
        try:
            self.db_cur.execute("ALTER TABLE student DROP INDEX student_id_idx")
            print("Index deleted successfully")
        except Exception as e:
            print(e)

    def explain(self):
        """
        Description: This function is to check the details of searching.
        
        """
        try:
            print("With indexing")
            self.db_cur.execute("EXPLAIN SELECT * FROM student WHERE name = 'Sam'")
            print("(id, select_type, table, partitions, type, possible_keys, key, ref, rows, filtered, extra)")
            for details in self.db_cur:
                print(details)


            #print("\n Without indexing")

            #self.db_cur.execute("EXPLAIN SELECT * FROM student WHERE name = 'Sam'")
            #print("(id, select_type, table, partitions, type, possible_keys, key, ref, rows, filtered, extra)")
            #for details in self.db_cur:
                #print(details)
        except Exception as e:
            print(e)


    







if __name__ == '__main__':
    index = Indexes()
    index.create_index()
    index.show_indexes()
    index.drop_index()
    index.show_indexes()
    index.explain()
    #index.drop_index()
    #print("After deletion")
    #index.explain()