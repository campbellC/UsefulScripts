import threading
from secondTimer import SecondTimer

class Pomodoro:
    def __init__(self, pomodoroLength=25, shortRestLength=5, longRestLength=15):
        self.pomodoroNumber = 0
        self.pomodoroLength = pomodoroLength
        self.shortRestLength = shortRestLength
        self.longRestLength = longRestLength
        self.currentTimeLeft = pomodoroLength * 1 #Debug change to 60

        self.secondTimerStopFlag = None
        self.secondTimer = None
        self.pomodoroTimer = None
        self.lock = threading.Lock()
        self.active = False


    def getCurrentSeconds(self):
        return self.currentTimeLeft % 60

    def getCurrentMinutes(self):
        return self.currentTimeLeft // 60

    def start(self):
        with self.lock:
            print "Pomodoro Started",self.active #DEBUG
            self.active = True
            self.pomodoroTimer = threading.Timer(self.currentTimeLeft, self.finished)
            self.pomodoroTimer.daemon = True
            self.pomodoroTimer.start()

            self.secondTimerStopFlag = threading.Event()
            self.secondTimer = SecondTimer(self.secondTimerStopFlag, self.clockTick)
            self.secondTimer.daemon = True
            self.secondTimer.start()

    def finished(self):
        with self.lock:
            self.active = False
            print "Pomodoro finished" #Debug
            if self.secondTimer is not None:
                self.secondTimerStopFlag.set()
            self.pomodoroNumber += 1
            self.pomodoroNumber = self.pomodoroNumber % 8
            self.currentTimeLeft = self.getNextPomodoroLength()
            print "starting UI" #DEBUG
            self.view.updateUIOnFinish()
            print "Finished UI" #DEBUG

    def stopTimers(self):
        with self.lock:
            print "stopTimers"
            if self.pomodoroTimer is not None:
                self.pomodoroTimer.cancel()

            if self.secondTimer is not None:
                self.secondTimerStopFlag.set()


    def clockTick(self):
        with self.lock:
            if self.active:
                print "clockTick"
                self.currentTimeLeft -= 1
                print "starting UIclock" #DEBUG
                self.view.updateUI()
                print "finishing  UIclock" #DEBUG
            else:
                pass

    def pause(self):
        self.stopTimers()
        with self.lock:
            self.view.updateUI()

    def skip(self):
        self.stopTimers()
        self.finished()

    def setView(self, view):
        self.view = view

    def getNextPomodoroLength(self):
        if self.pomodoroNumber % 2 == 0:
            return self.pomodoroLength
        if self.pomodoroNumber % 7 == 0:
            return self.longRestLength
        return self.shortRestLength

