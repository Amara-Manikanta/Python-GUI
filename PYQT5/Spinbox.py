import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Times", 12)


class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Spinboxes")
        self.setGeometry(50, 50, 350, 350)
        self.UI()

    def UI(self):
        self.spinBox=QSpinBox(self)
        self.spinBox.move(150,100)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(25)
        self.spinBox.setMaximum(100)
        self.spinBox.setRange(25,110)
        #self.spinBox.setPrefix("$")
        self.spinBox.setSuffix(" cm")
        self.spinBox.setSingleStep(5)
        #self.spinBox.valueChanged.connect(self.getValues)
        sendButton=QPushButton("Send",self)
        sendButton.move(150,140)
        sendButton.clicked.connect(self.getValues)
        self.show()


    def getValues(self):
        value=self.spinBox.value()
        print(value)




def main():
    App = QApplication(sys.argv)
    window = Windows()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()

