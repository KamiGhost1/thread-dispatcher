import time

class Task:
    id=""
    initTime=0
    finishTime=0
    result = ""
    initTasks=[]
    nextTasks=[]
    P,L = 0,0
    started = False
    finished = False

    def __init__(self, id, P, L, initTasks, nextTasks):
        self.id = id
        self.P = P
        self.L = L
        self.initTasks = initTasks
        self.nextTasks = nextTasks

    def start(self):
        self.initTime = time.time()
        self.started = True
        # threading.thread(target=self.func)
        #

    def finish(self):
        self.finishTime = time.time() - self.initTime
        self.finished = True