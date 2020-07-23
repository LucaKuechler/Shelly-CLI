#import db_fastScript
import os


class db_command_list():
    global_items = []

    def __init__(self):
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.items = []
        control_path = "Functions"
        home_path = "data_script"

        #started from cur path
        if control_path not in self.path:
            if home_path in self.path: 
                self.path = os.path.abspath(self.path + "\\..\\") 

            self.path += "\\Functions"
        

    #region staticmethods
    @staticmethod
    def get_files(path):
        ''' returns all files that are listed inside the path folder '''
        items = os.listdir(path)
        files = []
        for i in items:
            if "." in i:
                files.append(i)
        return files


    @staticmethod
    def get_section_name(path):
        ''' take the whole path and return only the last element because 
            this must be the parent folder for the selected file 
        '''

        path_li = path.split("\\")
        counter = len(path_li) - 1
        li = path_li[counter]
        return li


    @staticmethod
    def get_sections(path):
        ''' Get a path from a folder and call get_files() -> to get the files inside, 
            aswell as call get_section_name() -> to get the section name.
            Then store everything in a new list and return it.

            1.File = [File_Name | Section | Path]
        '''
        class_files = []
        files = db_command_list.get_files(path)
        class_section = db_command_list.get_section_name(path)

        for f in files:     
            class_file = []
            class_file.append(f) #Command-Name
            class_file.append(class_section) #Section-Name
            class_file.append(path) #path
            class_files.append(class_file)
        return class_files
    #endregion


    @classmethod
    def globalize_items(cls, items):
        ''' Add all items to the class variable global_items so that it can be called 
            from everyvery after a instance was created from the main.py file'''
        cls.global_items = items


    #region main loop
    def loop_sections(self):
        ''' Get all Folders from the objects path and store it in main_folders.
            delete the first path because it will be the parent of all main_folders.
            Each Folder in List should return his files. All These Files will be stored in a list
            and then returned
        '''
        path = self.path
        main_folders = [x[0] for x in os.walk(path)] 
        main_folders.pop(0)
        items = []

        for p in main_folders:
            item = db_command_list.get_sections(p)
            items += item

        self.items = items
        self.globalize_items(self.items)

        # for x in items:
        #     print(x)
    #endregion
    



class db_script_list():
    def __init__(self):
        pass