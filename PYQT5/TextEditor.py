import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Times", 14)


class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Spinboxes")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        self.editor=QTextEdit(self)
        self.editor.move(150,80)
        sendButton=QPushButton("Send",self)
        self.editor.setAcceptRichText(False)
        sendButton.move(330,280)
        sendButton.clicked.connect(self.getValue)


        self.show()

    def getValue(self):
        text=self.editor.toPlainText()
        print(text)








def main():
    App = QApplication(sys.argv)
    window = Windows()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()

