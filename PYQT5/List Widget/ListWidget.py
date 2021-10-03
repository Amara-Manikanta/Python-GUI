import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

font = QFont("Times", 14)


class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Spinboxes")
        self.setGeometry(50, 50, 500, 500)
        self.UI()

    def UI(self):
       self.addRecord=QLineEdit(self)
       self.addRecord.move(100,50)
       self.listwidget=QListWidget(self)
       self.listwidget.move(100,80)
       list1=["Iron Man",'Hulk','Loki']
       self.listwidget.addItems(list1)

       buttonAdd=QPushButton("Add",self)
       buttonAdd.move(360,80)
       buttonAdd.clicked.connect(self.funcadd)
       buttonDelete=QPushButton("Delete",self)
       buttonDelete.move(360,110)
       buttonDelete.clicked.connect(self.funcdel)
       buttonGet=QPushButton("Get",self)
       buttonGet.move(360,140)
       buttonGet.clicked.connect(self.funcget)
       buttonDeleteAll=QPushButton("Delete All",self)
       buttonDeleteAll.move(360,170)
       buttonDeleteAll.clicked.connect(self.funcDeleteAll)


       self.show()


    def funcadd(self):
        value=self.addRecord.text()
        self.listwidget.addItem(value)
        self.addRecord.setText("")

    def funcdel(self):
        id=self.listwidget.currentRow()
        print(id)
        self.listwidget.takeItem(id)
    def funcget(self):
        val=self.listwidget.currentItem().text()
        print(val)

    def funcDeleteAll(self):
        self.listwidget.clear()








def main():
    App = QApplication(sys.argv)
    window = Windows()

    sys.exit(App.exec_())


if __name__ == '__main__':
    main()

