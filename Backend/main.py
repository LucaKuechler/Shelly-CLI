import cmd
import shell
import time
import os
from data_script import db
from data_script import data_list
from data_script import db_commands
#import CommandList
#import ScriptList

#Main
class Program(shell.Shell):

    ''' system function '''

    def main(self, list_input):
        #call database
        path = os.path.dirname(os.path.realpath(__file__))
        path = path + "\\data_script\\command.db"
        db.Database().set_path(path)

        #setup data_list
        data_context = data_list.db_command_list()
        data_context.loop_sections()
        db_commands.DB_Commands().editing_loop()



#region Main Loop
if __name__ == '__main__':
    while True:
        Object = Program()
        status = Object.call_shell()
        list_input = Object.get_list()
        list_struc = Object.get_struc()

        t0 = time.time()
        if status == False:
            break
        else:
            Program().main(list_input)
            t1 = time.time()
            total = t1 - t0
            print(f"{total} secconds")

#endregion


    