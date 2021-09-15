import sys
from PyQt5.QtWidgets import *

class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Line Edits")
        self.setGeometry(50,50,350,350)
        self.UI()

    def UI(self):
        self.nameTextBox= QLineEdit(self)
        self.nameTextBox.setPlaceholderText("Please enter Your Name")
        self.nameTextBox.move(120,50)
        self.passTextBox=QLineEdit(self)
        self.passTextBox.setPlaceholderText("Please enter your password")
        self.passTextBox.setEchoMode(QLineEdit.Password)
        self.passTextBox.move(120,80)
        savebutton=QPushButton("Save",self)
        savebutton.move(180,110)

        savebutton.clicked.connect(self.getValues)
        self.show()

    def getValues(self):
        name = self.nameTextBox.text()
        password = self.passTextBox.text()
        self.setWindowTitle("Your name is : "+name +" Your password is : "+password)


def main():
    App=QApplication(sys.argv)
    window =Windows()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()

