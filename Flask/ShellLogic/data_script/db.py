import sqlite3
import os

class Database():
    path = ""
    def __init__(self):
        #cur_dir = os.path.dirname(os.path.realpath(__file__))
        #self.cur_dir = cur_dir + "\\command.db"
        pass


    @classmethod
    def commit(cls):
        ''' Just a quick way to commit things to the database. '''
        cls.connection.commit()


    @classmethod
    def close(cls):
        ''' Just a quick way to close the database connection. '''
        cls.connection.close()


    @classmethod
    def create(cls): 
        ''' This method creates the Database.
            It opens up an empty query an creates the commands and scripts table.
            Atfer this is done the connection will be closed
        '''

        cls.connection = sqlite3.connect(cls.path)
        query = cls.connection.cursor()
        
        query.execute('''CREATE TABLE commands (
            ID integer PRIMARY KEY AUTOINCREMENT,
            FileName text NOT NULL,
            Section Not Null,
            Path text Not Null
        )''')

        query.execute('''CREATE TABLE scripts (
        ID integer PRIMARY KEY AUTOINCREMENT,
        ScriptName text NOT NULL,
        ExecuteName text NOT NULL UNIQUE,
        ScriptStructure text NOT NULL
        )''')

        cls.commit()
        cls.close()
        print("file created")


    @classmethod
    def get_string(cls):
        ''' This function needs to be called if you want to setup a database connection.
            If the datbase allready exists the connenction string will be set.
            Otherwise the file will be created and the create() method will be executed.
            It also returns the connection string in case you want to work with the database.
        '''

        if cls.path == "":
            path = os.path.dirname(os.path.realpath(__file__))
            cls.path = path + "\\command.db"

        if os.path.exists(cls.path) == False:
            cls.create()
        
        cls.connection = sqlite3.connect(cls.path)

        print("Done")
        return cls.connection


    @classmethod
    def set_path(cls, path):
        ''' If this function is called from outside the file the path
        needs to be set first. Otherwise the databse can not be found '''
        cls.path = path










