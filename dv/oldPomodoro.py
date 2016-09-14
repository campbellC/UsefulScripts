#!/usr/bin/env python
import sys
import threading
import sounddevice
import soundfile
from PyQt4.QtCore import pyqtSlot, Qt, QPoint
from PyQt4.QtGui import *



# Create Window
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('Chris\' Pomodoro Timer')
w.move(QPoint(0,0))
#Create main layout
layout = QVBoxLayout(w)

# Create Box for Counter
textbox = QLineEdit()
textbox.setReadOnly(True)
layout.addWidget(textbox)

#Create a button
btn = QPushButton('Start next pomodoro')
layout.addWidget(btn)
#Numebrs
pomodoroNumber = 0
pomodoroLength = 25
smallRestLength = 5
longRestLength = 15
textbox.setText(str(pomodoroLength))

# Set up Sound File
def playAlarm():
    data, fs = soundfile.read("/System/Library/Sounds/Glass.aiff")
    sounddevice.play(data, fs, blocking=True)

lengthTillEnd = pomodoroLength
def reduceByOne():
    global lengthTillEnd
    lengthTillEnd -= 1
    textbox.setText(str(lengthTillEnd))
#Repeater
class Repeater(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(1 * 60):
            reduceByOne()


# logic for Pomodoro numbers
stopFlag = threading.Event()

def getNextPomodoroLength():
    global pomodoroNumber
    if pomodoroNumber % 2 == 0:
        return pomodoroLength
    else:
        if pomodoroNumber % 7 == 0:
            return longRestLength
        else:
            return smallRestLength

buttonPressLock = threading.Lock()
def endPomodoro():
    global pomodoroNumber
    global stopFlag
    playAlarm()
    pomodoroNumber += 1
    stopFlag.set()
    textbox.setText( str(getNextPomodoroLength()) )
    buttonPressLock.release()


#Create the actions
@pyqtSlot()
def startPomodoro():
    if not buttonPressLock.locked():
        global stopFlag
        buttonPressLock.acquire()
        global lengthTillEnd
        lengthTillEnd = getNextPomodoroLength()
        x = threading.Timer(lengthTillEnd * 60, endPomodoro )
        x.start()
        stopFlag = threading.Event()
        repeaterThread = Repeater(stopFlag)
        repeaterThread.start()

#connect signals to slots
btn.clicked.connect(startPomodoro)








# show window and run
w.show()
app.exec_()


