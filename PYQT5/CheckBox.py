import sys
from PyQt5.QtWidgets import *

class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using checkbox")
        self.setGeometry(50,50,350,350)
        self.UI()

    def UI(self):
       self.name=QLineEdit(self)
       self.name.setPlaceholderText("Enter your name")
       self.surname=QLineEdit(self)
       self.surname.setPlaceholderText("Enter your Surname")
       self.name.move(150,50)
       self.surname.move(150,80)
       self.remember=QCheckBox("Remember me",self)
       self.remember.move(150,110)
       submitbutton=QPushButton('Submit',self)
       submitbutton.move(200,140)
       submitbutton.clicked.connect(self.submit)
       self.show()
    def submit(self):
        if (self.remember.isChecked()):
            print("Name : "+self.name.text()+"\nSurname: "+ self.surname.text()
                  +"\nRemeber me Checked")
        else:
            print("Name : " + self.name.text() + "\nSurname: " + self.surname.text()
                  + "\nRemeber me not Checked")

def main():
    App=QApplication(sys.argv)
    window =Windows()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()

