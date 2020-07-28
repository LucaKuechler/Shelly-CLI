''' All system functions like cd or create remove and so on will be added here '''
import time

class sys_functions():

    def __init__(self):
        self.dir = ""
        self.output = ""
        self.dict = {
            "cur_dir" : self.dir,
            "cur_output" : self.output
        }


    def cd(self):
        newpath = "\\Hello\\Iam\\A\\Path"
        self.dict['cur_dir'] = newpath
        return self.dict


    def md(self):
        pass

