import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

font = QFont("Times", 14)


class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Spinboxes")
        self.setGeometry(250, 150, 350, 350)
        self.UI()

    def UI(self):
        self.colorLabel=QLabel(self)
        self.colorLabel.resize(250,250)
        self.colorLabel.setStyleSheet("background-color:green")
        self.colorLabel.move(40,20)
        #####################Buttons###################
        startbutton=QPushButton("Start",self)
        startbutton.move(80,300)
        startbutton.clicked.connect(self.start)
        stopButton=QPushButton("Stop",self)
        stopButton.move(190,300)
        stopButton.clicked.connect(self.stop)

        ############timer########################
        self.timer=QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.changecolor)
        self.value=0




        self.show()

    def changecolor(self):
        if self.value==0:
            self.colorLabel.setStyleSheet("background-color:yellow")
            self.value=1
        else:
            self.colorLabel.setStyleSheet("background-color:red")
            self.value = 0

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()







def main():
    App = QApplication(sys.argv)
    window = Windows()

    # to start by default we give here
    window.start()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()

