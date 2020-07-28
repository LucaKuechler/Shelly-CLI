import os

class DisplayDataList():
    def __init__(self):
        self.DisplayList = []
        self.counter = 0
        self.curDir = "/"

    def getData(self):
        return self.DisplayList


    def setData(self, input_field):
        # dir / user / command / output
        elem = [input_field[0], input_field[1], input_field[2], input_field[3]]
        self.DisplayList.append(elem)
        self.counter += 1


class InputDataElement():
    def __init__(self):
        # contains "user / dir / command / output"
        self.InputParts = []
        self.user = os.getlogin()
        self.dir = "/"
        self.command = ""
        self.output = ""
        self.timer = 0


    def setData(self, Parts):
        self.dir = Parts[0]
        self.command = Parts[1]
        self.output = Parts[2] 
        self.timer = Parts[3]


    def getData(self):
        self.InputParts.append(self.user)
        self.InputParts.append(self.dir)
        self.InputParts.append(self.command)
        self.InputParts.append(self.output)
        self.InputParts.append(self.timer)
        return self.InputParts
