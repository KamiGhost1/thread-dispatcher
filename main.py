import time
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import qIsNull
from PyQt5.QtWidgets import QApplication
from PyQt5.uic.properties import QtCore
import methods

import threading

Form, _ = uic.loadUiType('form.ui')

TaskCounter = 0 
lock = threading.Lock()
LOGG = ''
startTime = 0

class Ui(QtWidgets.QMainWindow, Form):
    tasks = dict()
    
     
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Button1Pressed)
        self.pushButton_2.clicked.connect(self.Button2Pressed)
        

    def Button1Pressed(self):
        global startTime
        self.logger("START")
        if len(self.tasks) > 0:
            self.tasks.clear()
            print("Clean task array")
        print("START")
        self.initTask()
        x = threading.Thread(target=self.firstStart, daemon=True)
        startTime = time.time()
        x.start()
        while TaskCounter < len(self.tasks):
            time.sleep(0.05)
            self.viewLogs()

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
        global LOGG
        global TaskCounter
        global startTime
        task.start()
        self.globalLogger("proccess " + task.id + " started in " + str(time.time()-startTime))
        self.searchTask(task.id)
        task.finish()
        self.globalLogger("proccess " + task.id + " finish in " + str(time.time()-startTime))
        TaskCounter+=1
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
                a = runList[i]
                localThreads[runList[i].id]=threading.Thread(target=self.startThread, args=(a,))
            for i in localThreads:
                localThreads[i].start()
            stop = False
            count = 0
            while(stop == False):
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
        log = self.textBrowser.toPlainText()
        log += logs + "\n"
        self.textBrowser.setText(log)
        
    def globalLogger(self, log):
        global LOGG
        global lock
        with lock:
            LOGG += log +"\n"
            print(log)

    def viewLogs(self):
        global LOGG
        self.textBrowser.setText(LOGG)
    

    def genM(self):
        time.sleep(3)
        return 0
    def genR(self):
        time.sleep(3)
        return 0 
    def F1(self):
        time.sleep(5)
        return 0 
    def F2(self):
        time.sleep(3)
        return 0 
    def F3(self):
        time.sleep(3)
        return 0 
    def F4(self):
        time.sleep(3)
        return 0 
    def F5(self):
        time.sleep(3)
        return 0 
    def F6(self):
        time.sleep(3)
        return 0 
    def F7(self):
        time.sleep(3)
        return 0 
    



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
