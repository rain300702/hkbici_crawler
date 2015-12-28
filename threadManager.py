# -*- coding: utf-8 -*-

import threading
import Queue


class WorkingThread(threading.Thread):
    '''
    This class defines how threads in this program should work.
    '''

    def __init__(self,threadManager):
        threading.Thread.__init__(self)
        self.threadManager = threadManager
        self.daemon = True

    def run(self):
        while True:
            try:
                func, args, kw = self.threadManager.getTask(timeout=1)
                result = func(*args,**kw)
                if result:
                    self.threadManager.putTask(self.threadManager.resultFunc,result)
                self.threadManager.taskDone()
            except Queue.Empty:
                break

class ThreadManager(object):
    '''
    This class manages threads created.
    '''

    def __init__(self,threadNum,resultFunc):
        self.threadNum = threadNum
        self.workQueue = Queue.Queue()
        self.resultFunc = resultFunc
        self.threadList = []

    def startThread(self):
        for i in range(self.threadNum):
            thread = WorkingThread(self)
            self.threadList.append(thread)
            thread.start()

    def blockThread(self):
        for thread in self.threadList:
            thread.join()

    def putTask(self,func,*args,**kw):
        self.workQueue.put((func,args,kw))

    def getTask(self,*args,**kw):
        return self.workQueue.get(*args,**kw)

    def taskDone(self):
        self.workQueue.task_done()
