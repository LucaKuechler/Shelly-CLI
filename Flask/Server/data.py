import os

class DisplayDataList():
    def __init__(self):
        self.DisplayList = []
        self.counter = 0
        self.curDir = "/"
        self.user = "@" + os.getlogin()

    def getData(self):
        return self.DisplayList


    def setData(self, input_field):
        # 0:dir / 1:command / 2:output / 3:time
        self.curDir = input_field[0]
        elem = [self.user, input_field[0], input_field[1], input_field[2], input_field[3]]
        self.DisplayList.append(elem)
        self.counter += 1


    def clearData(self):
        self.DisplayList = []

