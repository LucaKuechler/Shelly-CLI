import sqlite3
from ShellLogic.data_script import db
import os
from ShellLogic.data_script import data_list

class DB_Commands():
    def __init__(self):
        self.connection = db.Database().get_string()
        self.query = self.connection.cursor()
        self.items = data_list.db_command_list().global_items
     

    def check_exsitens(self):

        query = self.connection.cursor()
        query.execute("SELECT * FROM commands")
        row_data = query.fetchall()
        for row in row_data:
            name = row[1]
            path = row[3] + "\\" + name

            if os.path.exists(path) == False:
                sql_delete_query = """DELETE from commands where ID = ?"""
                query.execute(sql_delete_query, (row[0], ))
                self.connection.commit()
                self.query.close()
            else:
                pass# print(name)

        


    #region database manipulation 0 | 1 | 2
    def check_database(self, item):
        ''' Search a element name in the database and store its data.
            Then compare the data to the given item and return the status:
            #row data is same = 2
            #row data is there but different = 1
            #row data doesnt exist = 0
        '''

        try:
            self.query = self.connection.cursor()
            ID = item[0]

            self.query.execute("SELECT * FROM commands WHERE FileName=?", (ID,))
            row_data = self.query.fetchall()
            self.query.close()
            
            row_data = row_data[0]
            row_data = row_data[1:4]
            compare = []

            for x in range(0, len(row_data),1):
                if row_data[x] == item[x]:
                    compare.append(True)
                else:
                    compare.append(False)
            for comp in compare:
                if comp == False:
                    return 1

            return 2
        except:
            return 0
            

    def insert_commands(self, item):
        '''This fucntion is called if a specific item doesnt exist in the database.
            The item will eb added with Real_ID File_Name Section and the Path.
            ID will be set automatically from the database itself.
            After that the created query will be closed and executed.         
        '''

        self.query = self.connection.cursor()
        ID = None
        FileName = item[0]
        Section = item[1]
        Path = item[2]

        sqlite_select_query = '''INSERT INTO commands
        (ID, FileName, Section, Path)
        VALUES
        (?,?,?,?)
        '''
        data_tuple = (ID, FileName, Section, Path)

        self.query.execute(sqlite_select_query,data_tuple)
        self.connection.commit()
        self.query.close()
        print("input done")

        
    def update_commands(self, item):
        ''' Is just called if item in database is not up to date.
            Creates a new query and searchs for the element with the given ID.
            The element will be synchronised with the item list.
            After Updating the database the query is closed.
        '''

        self.query = self.connection.cursor()

        FileName = item[0] 
        Section = item[1] 
        Path = item[2] 

        sqlite_select_query = '''UPDATE commands set Section = ? where FileName = ?'''
        data_tuple = (Section, FileName)
        self.query.execute(sqlite_select_query, data_tuple)
        self.connection.commit()
        self.query.close()
        print("updated")
    #endregion


    def editing_loop(self):
        ''' Checks for each item in the list if it is allready in the datbase
            or it needs to be updated or inserted.
            If the item needs an update update_command() is called.
            If the item doesnt exist in the Database it will be added. 
            After executing database connection will be closed. 
        '''

        for item in self.items:
            value = self.check_database(item)
            if value == 2:
                pass
            elif value == 1:
                self.update_commands(item)
            else:
                self.insert_commands(item)

        self.check_exsitens()
        self.connection.close()
        

                
