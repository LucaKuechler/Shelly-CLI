import os

class DisplayDataList():
    def __init__(self):
        self.DisplayList = []
        self.counter = len(self.DisplayList)


    def getData(self):
        return self.DisplayList


    def setData(self, input_field):
        elem = [input_field[0], input_field[1], input_field[2], input_field[3]]
        self.DisplayList.append(elem)


class InputDataElement():
    def __init__(self):
        # contains "user / dir / command / output"
        self.InputElement = []
        self.user = ""
        self.dir = "/"
        self.command = ""
        self.output = ""
        self.fillData()


    def getData(self):
        self.InputElement.append(self.user)
        self.InputElement.append(self.dir)
        self.InputElement.append(self.command)
        self.InputElement.append(self.output)
        return self.InputElement

    
    def fillData(self):
        self.user = os.getlogin()
        self.dir = "/E/"
        self.command = "cd Hello"
        self.output = ""
