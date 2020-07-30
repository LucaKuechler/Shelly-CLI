''' All system functions like cd or create remove and so on will be added here '''
import os.path

class sys_functions():

    def __init__(self):
        self.dir = ""
        self.output = ""
        self.dict = {
            "cur_dir" : self.dir,
            "cur_output" : self.output
        }

        dr = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        self.drives = [d for d in dr if os.path.exists(f'{d}:')]



    def cd(self, args):
        if self.dir == "/" and args[0] in self.drives:
            self.dict['cur_dir'] = self.dir + args[0] + ":" + "/"
            return self.dict

        newpath = self.dir
        self.dict['cur_dir'] = newpath + args[0] + "/"
        cmd_path = os.path.abspath(self.dict['cur_dir'][1:])
        if os.path.exists(cmd_path):
            print(cmd_path)
            return self.dict
        return None
        



    def md(self):
        pass

