from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber
from PyQt5.QtCore import QTimer, QTime
from main import *
import sys
from PyQt5.QtGui import QKeySequence

class Timer(QMainWindow):
     timerMode = False
     counter = 0
     def __init__(self):
          super().__init__()
          self.ui = Ui_MainWindow()
          self.ui.setupUi(self)
          self.timer = QTimer()
          self.time = QTime()
          self.timer.timeout.connect(self.updateClock)
          self.ui.startClockButton.clicked.connect(self.startClockTimer)
          self.ui.startTimerButton.clicked.connect(self.startTimer)
          self.ui.stopTimerButton.clicked.connect(self.stopTimer)
          self.ui.resetTimerButton.clicked.connect(self.resetTimer)
          self.ui.pauseTimerButton.clicked.connect(self.pauseTimer)
          self.ui.resumeTimerButton.clicked.connect(self.resumeTimer)
          #self.ui.lcdDisplay.setSegmentStyle(QLCDNumber.Flat)
          self.startClockTimer()
          self.ui.actionFullScreen.triggered.connect(lambda:self.showFullScreen())
          self.ui.actionFullScreen.setShortcut("F11")
          self.ui.actionNormalScreen.triggered.connect(lambda:self.showNormal())
          self.ui.actionNormalScreen.setShortcut("F10")
          self.ui.actionExit.triggered.connect(lambda:exit())
          self.ui.actionExit.setShortcut("Ctrl+E")
          self.showNormal()


     def resumeTimer(self):
          self.timer.start(1000)


     def pauseTimer(self):
          self.timer.stop()

          
     def resetTimer(self):
          self.counter = 0
          self.ui.lcdDisplay.setDigitCount(5)
          self.ui.lcdDisplay.display(str(f"{0:02d}:{0:02d}"))
          self.timer.stop()


          
     def stopTimer(self):
          self.timer.stop()
          self.counter = 0



     def startTimer(self):
          self.timerMode = True
          self.timer.start(1000)


          
     def startClockTimer(self):
          self.timerMode = False
          self.timer.start(1000)

          
          
     def updateClock(self):
          if self.timerMode == False:
               self.ui.lcdDisplay.setDigitCount(11)
               print(self.time.currentTime().toString("hh:mm:ss ap"))
               self.ui.lcdDisplay.display(self.time.currentTime().toString("hh:mm:ss ap"))
          elif self.timerMode == True:
               self.ui.lcdDisplay.setDigitCount(5)
               self.counter = self.counter + 1
               hour , minutes = divmod(self.counter,60)
               self.ui.lcdDisplay.display(str(f"{hour:02d}:{minutes:02d}"))

app = QApplication(sys.argv)
timer = Timer()
timer.show()
sys.exit(app.exec_())
