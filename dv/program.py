import sys
from pomodoro import Pomodoro
from PyQt4.QtGui import *
from view import myWindow
from PyQt4.QtCore import QPoint

app = QApplication(sys.argv)

#Presets
pomodoroLength = 3
shortRestLength = 1
longRestLength = 2

#Set up window
window = myWindow()
window.move(QPoint(0,0))

#set up pomodoro
pomodoro = Pomodoro(pomodoroLength, shortRestLength, longRestLength)
window.setPomodoro(pomodoro)
pomodoro.setView(window)
window.updateUI()

window.show()
sys.exit(app.exec_())
