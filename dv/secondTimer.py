import threading

class SecondTimer(threading.Thread):
    def __init__(self,event,func):
        threading.Thread.__init__(self)
        self.stopped = event
        self.func = func

    def run(self):
        while not self.stopped.wait(1):
            self.func()
