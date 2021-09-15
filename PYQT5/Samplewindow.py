import sys
from PyQt5.QtWidgets import *

class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150,250,550,250)
        self.setWindowTitle("This is our Windows title")

        self.show()

App = QApplication(sys.argv)
window =Windows()
sys.exit(App.exec_())
