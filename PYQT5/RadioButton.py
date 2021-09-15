import sys
from PyQt5.QtWidgets import *

class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using comboboxes")
        self.setGeometry(50,50,350,350)
        self.UI()

    def UI(self):
       self.name=QLineEdit(self)
       self.name.move(150,50)
       self.name.setPlaceholderText("Enter Your Name")
       self.surname=QLineEdit(self)
       self.surname.move(150,80)
       self.surname.setPlaceholderText("Enter your Surname")
       self.male=QRadioButton("Male",self)
       self.female=QRadioButton("Female",self)
       self.male.move(150,110)
       self.female.move(200,110)
       submitButton=QPushButton("Submit",self)
       submitButton.clicked.connect(self.getValues)
       submitButton.move(200,140)

       self.show()

    def getValues(self):
        name=self.name.text()
        surname=self.surname.text()
        if self.male.isChecked():
            print(name+" "+surname+" You are a male")
        else:
            print(name + " " + surname + " You are a female")


def main():
    App=QApplication(sys.argv)
    window =Windows()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()

