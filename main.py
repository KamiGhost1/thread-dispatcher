import time
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import qIsNull
from PyQt5.QtWidgets import QApplication
from PyQt5.uic.properties import QtCore
import methods

import threading

Form, _ = uic.loadUiType('form.ui')



class Ui(QtWidgets.QMainWindow, Form):
    tasks = dict()
    
    global startTime
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Button1Pressed)
        self.pushButton_2.clicked.connect(self.Button2Pressed)
        

    def Button1Pressed(self):
        self.logger("START")
        if len(self.tasks) > 0:
            self.tasks.clear()
            print("Clean task array")
        print("START")
        self.initTask()
        x = threading.Thread(target=self.firstStart, daemon=True)
        y = threading.Thread(target=self.viewLogs, daemon=True)
        x.start()
        # y.start()

    def Button2Pressed(self):
        self.tasks.clear()
        print("RESET")
        self.logger("RESET")

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

    def buildTaskPull(self, servedPull):
        newPull = dict()
        pullConverted = list()
        elem = ''
        if len(servedPull) > 0:
            for i in range(len(servedPull)):
                elem = servedPull[i]
                if len(elem.nextTasks) > 0 :
                    for j in range(len(elem.nextTasks)):
                        if newPull.get(elem.nextTasks[j]) == None:
                            newPull[elem.nextTasks[j]] = self.tasks[elem.nextTasks[j]]
            for i in newPull:
                pullConverted.append(newPull[i])    
        return pullConverted

    def runner(self, runList):
        localThreads = dict()
        nextTaskPull = ''
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
                nextTaskPull = self.buildTaskPull(runList)
                if len(nextTaskPull) > 0:
                    self.runner(nextTaskPull)
                    # self.debugNewPull(nextTaskPull)
                else:
                    print("end of work ")


    def debugNewPull(self, newPull):
        for i in range(len(newPull)):
            print(newPull[i].nextTasks)

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

    def logger(self, logs):
        global log 
        log += logs + "\n"
        # QApplication.processEvents()
        self.viewLogs()
        
        
    def viewLogs(self):
        global log
        self.textBrowser.setText(log)
    
    def viewInfinityLogs(self):
        global log
        while True:
            self.textBrowser.setText(log)
            time.sleep(0.05)
    

    def genM(self):
        # self.logger("gen M start")
        time.sleep(3)
        # self.logger("gen M finish")
        return 0
    def genR(self):
        # self.logger("gen R start")
        time.sleep(3)
        # self.logger("gen R finish")
        return 0 
    def F1(self):
        # self.logger("F1 start")
        time.sleep(3)
        # self.logger("F1 finish")
        return 0 
    def F2(self):
        # self.logger("F2 start")
        time.sleep(3)
        # self.logger("F2 finish")
        return 0 
    def F3(self):
        # self.logger("F3 start")
        time.sleep(3)
        # self.logger("F3 finish")
        return 0 
    def F4(self):
        # self.logger("F4 start")
        time.sleep(3)
        # self.logger("F4 finish")
        return 0 
    def F5(self):
        # self.logger("F5 start")
        time.sleep(3)
        # self.logger("F5 finish")
        return 0 
    def F6(self):
        # self.logger("F6 start")
        time.sleep(3)
        # self.logger("F6 finish")
        return 0 
    def F7(self):
        # self.logger("F7 start")
        time.sleep(3)
        # self.logger("F7 finish")
        return 0 
    



if __name__ == '__main__':
    import sys
    global log
    log = ""
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
