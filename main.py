import time
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import qIsNull
from PyQt5.QtGui import QOpenGLVersionProfile
from PyQt5.QtWidgets import QApplication
from PyQt5.uic.properties import QtCore
import methods
import threading
import random
import numpy as np

Form, _ = uic.loadUiType('form.ui')


lock = threading.Lock()
lockM = threading.Lock()
lockR = threading.Lock()

TaskCounter = 0 
LOGG = ''
startTime = 0
N = 3
MAX_VALUE = 100
TRUE_VALUE = 0.5
M = [[0]*N]*N
R = [False]*N

class Ui(QtWidgets.QMainWindow, Form):
    tasks = dict()
    progressBars = dict()

    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Button1Pressed)
        self.pushButton_2.clicked.connect(self.Button2Pressed)
        

    def Button1Pressed(self):
        global startTime
        global TaskCounter
        global LOGG
        LOGG = ""
        # random.seed(26)
        self.globalLogger("START")
        if len(self.tasks) > 0:
            self.tasks.clear()
            print("Clean task array")
        print("START")
        self.initTask()
        x = threading.Thread(target=self.firstStart, daemon=True)
        startTime = time.time()
        x.start()
        
        while TaskCounter < len(self.tasks):
            self.viewLogs()
            for i in self.progressBars:
                if self.tasks[i].started and not self.tasks[i].finished:
                    self.progressBars[i].setValue(20)
                if self.tasks[i].finished and self.tasks[i].started:
                    self.progressBars[i].setValue(100)
        else:
            TaskCounter = 0
            self.printResults()
            self.viewLogs()
            self.protocol()


    def Button2Pressed(self):
        self.tasks.clear()
        print("RESET")
        self.globalLogger("RESET")

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
        self.progressBars["A"] = self.A
        self.progressBars["B"] = self.B
        self.progressBars["C"] = self.C
        self.progressBars["D"] = self.D
        self.progressBars["E"] = self.E
        self.progressBars["F"] = self.F
        self.progressBars["G"] = self.G
        self.progressBars["H"] = self.H
        self.progressBars["K"] = self.K
        for i in self.progressBars:
            self.progressBars[i].setValue(0)

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
        task.result = self.searchTask(task.id)
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
            return self.genM()
        if name == 'B':
            return self.genR()
        if name == 'C':
            return self.F1()
        if name == 'D':
            return self.F2()
        if name == 'E':
            return self.F3()
        if name == 'F':
            return self.F4()
        if name == 'G':
            return self.F5()
        if name == 'H':
            return self.F6()
        if name == 'K':
            return self.F7()

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
        global M, MAX_VALUE, lockM
        with lockM:
            localM = np.array(M)
        a = 0
        for i in range(N):
            for j in range(N):
                a = random.randint(0, MAX_VALUE)
                localM[i][j] = a
                # print(a)
        with lockM:
            M = localM
        time.sleep(1)
        return localM
    def genR(self):
        global R,TRUE_VALUE, lockR
        a = 0
        with lockR:
            localR = np.array(R)
        for i in range(N):
            a = random.random()
            if(a > TRUE_VALUE):
                localR[i]=True
            else:
                localR[i]=False
        with lockR:
            R = localR
        time.sleep(1)
        return localR
    def F1(self):
        global lockR, lockM, M, R
        with lockM:
            localM = np.array(M)
        with lockR:
            localR = np.array(R)
        for i in range(N):
            for j in range(N):
                # print(localM[i][j])
                # print(R)
                if localR[j]:
                    localM[i][j] +=5
        with lockM:
            M = localM
        time.sleep(1)
        return localM 
    def F2(self):
        global lockR, lockM, M, R
        with lockM:
            localM = np.array(M)
        with lockR:
            localR = np.array(R)
        for i in range(N):
            for j in range(N):
                if localR[j]:
                    localM[i][j] = round(localM[i][j]/2)
        with lockM:
            M = localM
        time.sleep(1)
        return localM  
    def F3(self):
        global lockR, lockM, M, R
        with lockM:
            localM = np.array(M)
        with lockR:
            localR = np.array(R)
        for i in range(N):
            for j in range(N):
                if localR[j]:
                    localM[i][j] *=3
        with lockM:
            M = localM
        time.sleep(1)
        return localM 
    def F4(self):
        res1 = self.F1()
        res2 = self.F2()
        res3 = self.F3()
        return [res1,res2,res3]  
    def F5(self):
        res1 = self.F1()
        res2 = self.F2()
        res3 = self.F3()
        return [res1,res2,res3]  
    def F6(self):
        res1 = self.F1()
        res2 = self.F2()
        res3 = self.F3()
        return [res1,res2,res3]  
    def F7(self):
        res = self.F5()
        return res 
    
    def printResults(self):
        global M, R, lockM, lockR
        self.globalLogger("\nRESULTS:\n")
        for i in range(N):
            for j in range(N):
                self.globalLogger(str(M[i][j]))
                print(M[i][j])
        self.globalLogger(str(R))
        print(R)
    
    def protocol(self):
        file = open("protocol.txt", "w")
        file.write("0;1;2;3;4;5\n")
        for i in self.tasks:
            protocol = '{};{};{};{};{};{}\n'.format(self.tasks[i].id,self.tasks[i].initTime - startTime, self.tasks[i].initTasks , self.tasks[i].result ,self.tasks[i].nextTasks ,self.tasks[i].finishTime )
            # print(protocol)
            file.write(protocol)
        pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
