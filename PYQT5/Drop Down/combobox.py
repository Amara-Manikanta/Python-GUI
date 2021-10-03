import sys
from PyQt5.QtWidgets import *

class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using comboboxes")
        self.setGeometry(50,50,350,350)
        self.UI()

    def UI(self):
       self.combo=QComboBox(self)
       self.combo.move(150,100)
       saveButton=QPushButton("Save",self)
       saveButton.move(150,130)
       saveButton.clicked.connect(self.getValue)
       self.combo.addItem("Python")
       self.combo.addItems(["C","C#","PHP"])
       list1=['Iron Man','Black Panther','Loki']
       for i in list1:
           self.combo.addItem(i)
       for j in range(1,10):
           self.combo.addItem(str(j))
       self.show()

    def getValue(self):
        value=self.combo.currentText()
        print(value)


def main():
    App=QApplication(sys.argv)
    window =Windows()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()

