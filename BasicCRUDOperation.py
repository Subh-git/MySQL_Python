'''
@Author: Subhadeep Bhattacharjee
@Date: 2021-12-17 11:00
@Title: This file contains a class and its method to show basic CRUD operation in mysql through python.

'''


import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

#dot env files are very much required to hide unnecessary information or security information 
# from getting displayed in code

class BasicCRUD():        #creating a class for performing basic crud operations


  def __init__(self):
    self.mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password= os.getenv("MySQL_Password"),
      auth_plugin='mysql_native_password'
      )
    
    self.db_cursor = self.mydb.cursor()   #creating a cursor which is used as to process what we are doing.

#creating a db
  def create_database(self, dbname):
    '''
    Description: 
      This method takes self and a database name as parameter that creates a database in mysql.
    Parameter:
      Self and the name of database.
    '''
    try:
      self.db_cursor.execute("CREATE DATABASE {0}".format(dbname))

    except Exception as e:
      print(e)

#showing all the present db
  def show_databases(self):
    '''
    Description:
      This shows all the available databases.
    '''
    self.db_cursor.execute("SHOW DATABASES")

    for db in self.db_cursor:
      print(db[0].decode())             #decode is used as the resultant is bytearray encrypted object.

#deleting a database
  def drop_database(self,dbname):
    '''
    Description:
      This deletes the specified database.
    '''
    try:
      self.db_cursor.execute("DROP DATABASE {0}".format(dbname))
      print("Database deleted successfully")

    except Exception as e:
      print(e)

#creating a table
  def create_table(self,dbname,table_name,schema):
    '''
    Description:
      This function create a table in the specified database.
    Parameter:
      This function takes 3 parameters, the database name where the table is to be created, the tbale name
      and the schema.    
    '''
    try:
      self.db_cursor.execute("USE {0}".format(dbname))
      self.db_cursor.execute("CREATE TABLE {0}({1})".format(table_name,schema))
      
    except Exception as e:
      print(e)

#show tables
  def show_tables(self, dbname):
    '''
    Description:
      This function shows all the available tables.
    '''
    try:
      self.db_cursor.execute("USE {0}".format(dbname))
      self.db_cursor.execute("SHOW TABLES")
      
      for i in self.db_cursor:
        print(i[0].decode())
    
    except Exception as e:
      print(e)

#drop table
  def drop_table(self,dbname, table_name):
    '''
    Description:
      This function drops the mentioned table.
    '''
    try:
      self.db_cursor.execute("USE {0}".format(dbname))
      self.db_cursor.execute("DROP TABLE {0}".format(table_name))
      print(f"{table_name} deleted succesfully")
    
    except Exception as e:
      print(e)

#describe table
  def describe_table(self,table_name):
    """
    Description: 
      This function is to describe the table created.
    """ 
    try:
        self.db_cursor.execute("DESCRIBE {0}".format(table_name))
        mycur = self.db_cursor.fetchall()

        for tableInfo in mycur:
          print(tableInfo)

    except Exception as e:
        print(e)

#inserting into table
  def insert_values(self,table_name, values):
    '''
    Description:
      This function enables us to insert into a table.
    Parameter:
      This takes self, table name and values as the parameter.
    '''
    try:
      self.db_cursor.execute("INSERT INTO {0} VALUES{1}".format(table_name,values))
      self.mydb.commit()
    
    except Exception as e:
      print(e)

#display the table content
  def display_all_values(self, table_name):
    '''
    Description:
      This function displays all the values from the given specified table.
    Parameter:
      This takes table_name as the parameter
    '''
    try:
      self.db_cursor.execute("SELECT * FROM {0}".format(table_name))
      result = self.db_cursor.fetchall()
      for i in result:
        print(i)
    
    except Exception as e:
      print(e)

#alter table
  def alter_table(self):
    '''
    Description:
      This function alters the table and can add constraints, columns etc.
    '''
    self.db_cursor.execute('''ALTER TABLE student ADD CONSTRAINT 
      FOREIGN KEY(course_id) REFERENCES course(course_id) ON DELETE SET NULL''')
    self.db_cursor.execute('ALTER TABLE student ADD score INT')
    self.mydb.commit()


#update table
  def update_table(self):
    '''
    Description:
      This updates a branch detail.
    '''
    self.db_cursor.execute('UPDATE course SET course_name = "English" WHERE course_id = 4')
    self.mydb.commit()    

#order by
  def order_ascending(self, table_name, columnname):
    '''
    Description:
      This function orders the table by the specified column name in ascending order. 
    '''
    self.db_cursor.execute("SELECT * FROM {0} ORDER BY {1}".format(table_name,columnname))
    mycur = self.db_cursor.fetchall()
    for i in mycur:
      print(i)




if __name__ == '__main__':
  basic = BasicCRUD()
  basic.create_database('college')
  basic.show_databases()
  #basic.drop_database('employee')
  #basic.drop_table('employee','EMP')
  schema_student = 'id INT PRIMARY KEY, name VARCHAR(20) NOT NULL, course_id INT'
  basic.create_table('college','student',schema_student)
  schema_course = 'course_id INT PRIMARY KEY, course_name VARCHAR(20) UNIQUE'
  basic.create_table('college','course',schema_course)
  basic.show_tables('college')

  #inserting into tables-----
  basic.describe_table('course')
  value_course = "(1, 'Physics'),(2, 'Chemistry'), (3, 'Mathematics'), (4, 'Biology')"
  basic.insert_values('course',value_course)
  basic.display_all_values('course')
  basic.update_table()
  basic.alter_table()
  basic.describe_table('student')
  value_student = "(10, 'Harry',2, 85), (11, 'Jim', 3, 72), (12, 'Ronald', 2, 98), (13, 'Sam', NULL, NULL)"
  basic.insert_values('student', value_student)
  basic.display_all_values('student')
  basic.order_ascending('student', 'score')
