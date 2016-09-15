import threading
from secondTimer import SecondTimer

class Pomodoro:
    def __init__(self, pomodoroLength=25, shortRestLength=5, longRestLength=15):
        self.pomodoroNumber = 0
        self.pomodoroLength = pomodoroLength
        self.shortRestLength = shortRestLength
        self.longRestLength = longRestLength
        self.currentTimeLeft = pomodoroLength * 60 #Debug change to 60

        self.secondTimerStopFlag = None
        self.secondTimer = None
        self.UIlock = threading.Lock()

    def getCurrentSeconds(self):
        return self.currentTimeLeft % 60

    def getCurrentMinutes(self):
        return self.currentTimeLeft // 60

    def start(self):

        self.secondTimerStopFlag = threading.Event()
        self.secondTimer = SecondTimer(self.secondTimerStopFlag, self.clockTick)
        self.secondTimer.daemon = True
        self.secondTimer.start()

    def finished(self):
        if self.secondTimer is not None:
            self.secondTimerStopFlag.set()
        self.pomodoroNumber += 1
        self.pomodoroNumber = self.pomodoroNumber % 8
        self.currentTimeLeft = self.getNextPomodoroLength()
        with self.UIlock:
            self.view.updateUIOnFinish()

    def clockTick(self):
        self.currentTimeLeft -= 1
        if self.currentTimeLeft == 0:
            self.finished()
        else:
            with self.UIlock:
                self.view.updateUI()

    def pause(self):
        self.secondTimerStopFlag.set()
        with self.UIlock:
            self.view.updateUI()

    def skip(self):
        self.finished()

    def setView(self, view):
        self.view = view

    def getNextPomodoroLength(self):
        if self.pomodoroNumber % 2 == 0:
            temp = self.pomodoroLength
        elif self.pomodoroNumber % 7 == 0:
            temp = self.longRestLength
        else:
            temp = self.shortRestLength
        return temp * 60

