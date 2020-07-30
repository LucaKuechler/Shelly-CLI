#import everyfolder with a init.py
from ShellLogic.Functions.basic_func import sys_functions



class func_code():

    def __init__(self):
        #system functions
        self.args = []
        self.struc = []
        self.cur_dir = ""
        self.win = sys_functions()
        win = self.win

        # cd = win.cd()
        # md = win.md()

        self.sys_funcs = {
            "cd" : win.cd,
            "md" : win.md
        }


        self.funcs = {
            
        }



    def create_execute_list(self, data_list):
        # Name | status | func
        '''  Just for external commands not for system'''
        self.executable_list = []



    def check_request(self, command):

        try:
            data = self.sys_funcs[command](self.args)
        
        except:
            print("Wrong")
            data = None

        return data

        



    def run_preset_dir(self, preset):
        pass


    def run_argument(self, argument):
        pass


    def runtime_loop(self, cur_dir, c_list, s_list):
        command = c_list.pop(0)
        s_list.pop(0)
        for arg in c_list:
            self.args.append(arg)
        self.cur_dir = cur_dir
        self.struc = s_list
        counter = 0
        print(self.args)
        for x in s_list:

            if x == "argument":
                self.run_argument(s_list[counter])

            elif x == "preset_dir":
                self.run_preset_dir(s_list[counter])

            else:
                continue

            counter += 1

        self.win.dir = cur_dir 
        data = self.check_request(command)
        return data



    def creation_loop(self, data_list):
        #self.create_execute_list(data_list)
        pass
