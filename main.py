import time
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication
import methods

import threading

Form, _ = uic.loadUiType('form.ui')



class Ui(QtWidgets.QMainWindow, Form):
    tasks = dict()
    threads = dict()
    global startTime
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Button1Pressed)
        self.pushButton_2.clicked.connect(self.Button2Pressed)

    def Button1Pressed(self):
        if len(self.tasks) > 0:
            self.tasks.clear()
            print("Clean task array")
        print("START")
        self.initTask()
        # self.debugList()
        # self.startThread(self.tasks["A"])
        global log
        log += "START\n"
        self.textBrowser.setText(log)
        self.firstStart()

    def Button2Pressed(self):
        self.tasks.clear()
        print("RESET")
        global log
        log = "RESET\n"
        self.textBrowser.setText(log)

    def initTask(self):
        self.tasks["A"] = methods.Task("A", 0, 1, [], ["C", "D", "E"])
        self.tasks["B"] = methods.Task("B", 0, 1, [], ["C", "D", "E"])
        self.tasks["C"] = methods.Task("C", 1, 1, ["A", "B"], ["F", "G", "H"])
        self.tasks["D"] = methods.Task("D", 1, 1, ["A", "B"], ["F", "G", "H"])
        self.tasks["E"] = methods.Task("E", 1, 1, ["A", "B"], ["F", "G", "H"])
        self.tasks["F"] = methods.Task("F", 2, 1, ["C", "D", "E"], [])
        self.tasks["G"] = methods.Task("G", 2, 1, ["C", "D", "E"], ["K"])
        self.tasks["H"] = methods.Task("H", 2, 1, ["C", "D", "E"], [])
        self.tasks["K"] = methods.Task("K", 3, 1, ["G"], [])

    def firstStart(self):
        runList = list()
        runList.append(self.tasks["A"])
        runList.append(self.tasks["B"])
        self.runner(runList)
        

    def startThread(self, task):
        print(task.id)
        task.start()
        self.searchTask(task.id)
        task.finish()
        print(task.finishTime)
        return 0

    def runner(self, runList):
        localThreads = dict()
        a=''
        if len(runList) > 0:
            for i in range(len(runList)):
                # print(runList[i].id)
                # self.startThread(runList[i])
                a = runList[i]
                localThreads[runList[i].id]=threading.Thread(target=self.startThread, args=(a,))
            for i in localThreads:
                localThreads[i].start()
            stop = False
            count = 0
            while(stop == False):
                # print("alallalalalallalalalalalalalalallalal")
                for i in localThreads:
                    if(localThreads[i].is_alive()):
                        stop = False
                    else:
                        count+=1
                if(count == len(localThreads)):
                    stop = True
                else:
                    count = 0
            else:
                print("end of work ")

        
    def debugList(self):
        for i in self.tasks :
            print(self.tasks[i].nextTasks)

    def searchTask(self, name):
        if name == 'A':
            self.genM()
        if name == 'B':
            self.genR()
        if name == 'C':
            self.F1()
        if name == 'D':
            self.F2()
        if name == 'E':
            self.F3()
        if name == 'F':
            self.F4()
        if name == 'G':
            self.F5()
        if name == 'H':
            self.F6()
        if name == 'K':
            self.F7()
        

    def genM(self):
        print("gen M start")
        time.sleep(10)
        print("gen M ready")
        return 0
    def genR(self):
        print("gen R start")
        time.sleep(3)
        print("gen R ready")
        return 0 
    def F1(self):
        return 0 
    def F2(self):
        return 0 
    def F3(self):
        return 0 
    def F4(self):
        return 0 
    def F5(self):
        return 0 
    def F6(self):
        return 0 
    def F7(self):
        return 0 
    



if __name__ == '__main__':
    import sys
    global log
    log = ""
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
