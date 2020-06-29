from Functions import basic_func
import os
import cmd
import time

class Shell:
    
    #region class variables
    ''' all type of constant values are defined here '''
    welcome = "Welcome to Shelly"
    begin = "[User] >"
    end = "quit"
    error = "error"


    ''' Ruleset '''
    argument_phrase = "#"
    preset_dir_phrase = "%"
    #endregion


    #region constructor
    def __init__(self):
        self.status = True  
        self.command_list = " "
        self.structure_list = " "
    #endregion


    #region create command structure
    def struc(self):

        ''' This function creates the current command structure.
            That means it checks if the input is and argument or a preset.
            The first letter of every word (not including the first one) could be an argument preset.
        '''

        self.structure_list = ["command"]

        for x in self.command_list:
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


    def final_input(self):
        # while True:
        #     cur_input = 
        # return cur_input
        pass
    #endregion


    #region creates input
    def read(self):
        ''' Ask for input and read it out after ENTER is pressed.
            Check if the user calls the end command.
            If anything went wrong while checking the data send error message
        '''

        command = input()
        command = command.strip()
        command = command.split() 

        try:
            if command[0] != "quit":
                return command
            else:
                self.status = False
        except:
            return self.error
    #endregion


    #region program loop
    def call_shell(self):
        ''' This function calls the read() function and saves the input list.
            After checking wheater their is any speacial command it calls the struct() function.
            The main part is to keep the loop going or interupt it. 
        '''

        self.command_list  = self.read()

        if self.command_list != self.error and self.status != False:
            self.structure_list = self.struc()
            return True
        else:   
            if self.status == True:          
                return True
            else:
                return False
    #endregion


    #region return
    '''commands'''
    def get_list(self):
        return self.command_list


    '''structure'''
    def get_struc(self):
        return self.structure_list
    #endregion