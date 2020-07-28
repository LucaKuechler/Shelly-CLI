from ShellLogic.Functions import func_list
import os
import cmd
import time
from ShellLogic.data_script import data_list

class Shell:
    
    #region class variables
    ''' all type of constant values are defined here '''
    end = "quit"
    error = "error"


    ''' Ruleset '''
    argument_phrase = "#"
    preset_dir_phrase = "%"
    script = "@"
    #endregion


    #region constructor
    def __init__(self):
        self.status = True  
        self.command_list = " "
        self.structure_list = " "
    #endregion



    def interpreter(self, cur_dir, c_list, s_list):
        ''' execution '''
        # global_items = data_list.db_command_list().global_items
        # func_list.func_code().creation_loop(global_items)
        data = func_list.func_code().runtime_loop(cur_dir, c_list, s_list)
        return data



    #region create command structure
    def struc(self):
        ''' This function creates the current command structure.
            That means it checks if the input is and argument or a preset.
            The first letter of every word (not including the first one) could be an argument preset.
        '''
        if self.script in self.command_list[0][0]:
            self.structure_list = ["script"]
            return self.structure_list

        self.structure_list = ["command"]

        for x in self.command_list:
            if x == self.command_list[0]:
                continue

            x = x[0] # set x = to first char

            if x == self.preset_dir_phrase:
                self.structure_list.append("preset_dir")
            elif x == self.argument_phrase:
                self.structure_list.append("argument")
            else:
                self.structure_list.append("parameter")
        return self.structure_list
    #endregion


    #region auto complete 
    def auto_complete(self):
        ''' This function will access the struc and input lists. 
            It returns the method including its input.
        '''
        pass 



    #region creates input
    def read(self, cur_command):
        ''' Ask for input and read it out after ENTER is pressed.
            Check if the user calls the end command.
            If anything went wrong while checking the data send error message
        '''
        input_data = cur_command.strip()
        input_data = cur_command.split() 

        try:
            if input_data[0] != "quit":
                return input_data
            else:
                self.status = False
        except:
            return self.error
    #endregion


    #region program loop
    def call_shell(self, cur_dir, cur_command):
        ''' This function calls the read() function and saves the input list.
            After checking wheater their is any speacial command it calls the struct() function.
            The main part is to keep the loop going or interupt it. 
        '''
        self.command_list = self.read(cur_command)

        if self.command_list != self.error and self.status != False:
            self.structure_list = self.struc()

        data = self.interpreter(cur_dir, self.get_list(), self.get_struc())
        return data
        
        
    #endregion


    #region return
    '''commands'''
    def get_list(self):
        return self.command_list


    '''structure'''
    def get_struc(self):
        return self.structure_list
    #endregion