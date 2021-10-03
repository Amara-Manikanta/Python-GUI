import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
font = QFont("Times",12)

class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using comboboxes")
        self.setGeometry(50,50,350,350)
        self.UI()

    def UI(self):
        clickButton=QPushButton("Click ME!",self)
        clickButton.setFont(font)
        clickButton.move(200,150)
        clickButton.clicked.connect(self.messageBox)
        self.show()

    def messageBox(self):
        #mbox =QMessageBox.information(self,"Information","You Logged out!")

        mbox = QMessageBox.question(self,"Warning!!!","Arue you sure to "
                                                  "exit?",QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,QMessageBox.No)
        if mbox==QMessageBox.Yes:
            sys.exit()
        elif mbox==QMessageBox.No:
            print("You have clicked No Button")
        







def main():
    App=QApplication(sys.argv)
    window =Windows()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()

