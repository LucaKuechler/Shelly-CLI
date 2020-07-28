#import everyfolder with a init.py
from ShellLogic.Functions import basic_func as win

class func_code():

    def __init__(self):
        #system functions
        self.args = []
        self.struc = []
        self.cur_dir = ""


        cd = win.cd()
        md = win.md()

        self.sys_funcs = {
            "cd" : cd,
            "md" : md
        }


        self.funcs = {
            
        }



    def create_execute_list(self, data_list):
        # Name | status | func
        '''  Just for external commands not for system'''
        self.executable_list = []




    def check_request(self, command):
        try:
            self.sys_funcs[command]
        except:
            try:
                self.funcs[command]
            except:
                print("eee")


    def run_preset_dir(self):
        pass


    def run_argument(self):
        pass


    def runtime_loop(self, cur_dir, c_list, s_list):
        command = c_list.pop(0)
        s_list.pop(0)
        for arg in c_list:
            self.args.append(arg)
        self.cur_dir = cur_dir
        self.struc = s_list
        
        for arg in self.args:
            if arg == "argument":
                self.run_argument()
            elif arg == "preset_dir":
                self.run_preset_dir()
            else:
                continue

        self.check_request(command)



    def creation_loop(self, data_list):
        #self.create_execute_list(data_list)
        pass
