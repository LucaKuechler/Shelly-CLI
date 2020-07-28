from ShellLogic import shell
import os
from ShellLogic.data_script import db
from ShellLogic.data_script import data_list
from ShellLogic.data_script import db_commands


#Main
class Program(shell.Shell):

    ''' system function '''


    def __init__(self):
        ''' Program class will only be created on program start. 
            1. Connect to Database
            2. Setup DataList
        '''
        self.cur_command = ""
        self.cur_dir = ""

        #call database
        path = os.path.dirname(os.path.realpath(__file__))
        path = path + "\\data_script\\command.db"
        db.Database().set_path(path)

        #setup data_list
        data_context = data_list.db_command_list()
        data_context.loop_sections()
        db_commands.DB_Commands().editing_loop()

        #shell
        self.prompt = shell.Shell()



    def main_loop(self):
        ''' Input will be given to shell. 
            The shell then returns then the output. 
        '''
        data = self.prompt.call_shell(self.cur_dir, self.cur_command)
        return data



    def insert_command(self, curdir, command):
        ''' Server sends his input to this method.
            The method will safe the input inside the class.
        '''
        self.cur_command = command
        self.cur_dir = curdir






    