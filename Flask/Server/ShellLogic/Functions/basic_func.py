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

        #set drive
        if args[0][0] in self.drives and ":" in (args[0][1]):
            print("money")
            self.dict['cur_dir'] = "/"+ args[0] + "/"
            return self.dict


        #cd backwards
        if self.dir != "/" and "." in args[0]: 
            x_counter = 0  #. 

            for x in args[0]:
                if x == ".":
                    x_counter += 1
                else:
                    return None

            dir_list = self.dir.split("/")
            dir_list = dir_list[1:-1]


            if len(dir_list) <= x_counter:
                self.dict["cur_dir"] = "/"
                return self.dict

            elif len(dir_list) > x_counter:
                new_dir = ""
                dir_list = dir_list[:-x_counter]

                for x in dir_list:
                    new_dir = new_dir + "/" + x
                self.dict['cur_dir'] = new_dir + "/"

                return self.dict

            else:
                return None

        elif self.dir == "/":
            return None


        else:
            self.dict['cur_dir'] = self.dir + args[0] + "/"
            cmd_path = os.path.abspath(self.dict['cur_dir'][1:])

            if os.path.exists(cmd_path):
                return self.dict
            return None
        



    def md(self):
        pass

