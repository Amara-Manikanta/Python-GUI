import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer
from random import randint

font = QFont("Times", 14)
buttonFont = QFont("Arial", 12)
computerScore = 0
playerScore = 0


class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Spinboxes")
        self.setGeometry(350, 150, 550, 500)
        self.UI()

    def UI(self):
        ############################Score Borad#############################
        self.scorecomputerText = QLabel("Computer Score : ", self)
        self.scorecomputerText.move(30, 20)
        self.scorecomputerText.setFont(font)
        self.scorePlayerText = QLabel("Your Score : ", self)
        self.scorePlayerText.setFont(font)
        self.scorePlayerText.move(330, 20)

        ##########################Images###################################

        self.imageComputer = QLabel(self)
        self.imageComputer.setPixmap(QPixmap("Images/rock.png"))

        self.imageComputer.move(50, 100)

        self.imagePlayer = QLabel(self)
        self.imagePlayer.setPixmap(QPixmap("Images/rock.png"))
        self.imagePlayer.move(330, 100)

        self.imagegame = QLabel(self)
        self.imagegame.setPixmap(QPixmap("Images/game.png"))
        self.imagegame.move(230, 145)

        ##################Buttons#########################

        startButton = QPushButton("Start", self)
        startButton.setFont(buttonFont)
        startButton.move(90, 250)
        startButton.clicked.connect(self.funcstart)
        stopButton = QPushButton("Stop", self)
        stopButton.setFont(buttonFont)
        stopButton.move(350, 250)
        stopButton.clicked.connect(self.funcstop)

        ######################Timer##########################
        self.timer = QTimer(self)
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.playGame)

        self.show()

    def playGame(self):
        self.rndcomputer = randint(1, 3)

        if self.rndcomputer == 1:
            self.imageComputer.setPixmap(QPixmap("Images/rock.png"))
        elif self.rndcomputer == 2:
            self.imageComputer.setPixmap(QPixmap("Images/paper.png"))
        else:
            self.imageComputer.setPixmap(QPixmap("Images/scissors.png"))

        self.rndplayer = randint(1, 3)
        if self.rndplayer == 1:
            self.imagePlayer.setPixmap(QPixmap("Images/rock.png"))
        elif self.rndplayer == 2:
            self.imagePlayer.setPixmap(QPixmap("Images/paper.png"))
        else:
            self.imagePlayer.setPixmap(QPixmap("Images/scissors.png"))

    def funcstart(self):
        self.timer.start()

    def funcstop(self):
        global computerScore
        global playerScore
        self.timer.stop()
        if (self.rndcomputer == 1 and self.rndplayer == 1) or (self.rndcomputer == 2 and self.rndplayer == 2) or (

                self.rndcomputer == 3 and self.rndplayer == 3):
            mbox = QMessageBox.information(self, "Information", "Draw Game")
        elif (self.rndcomputer == 1 and self.rndplayer == 2) or (self.rndcomputer == 2 and self.rndplayer == 3) or (

                self.rndcomputer == 3 and self.rndplayer == 1):
            mbox = QMessageBox.information(self, "Information", "you win!")
            playerScore += 1
            self.scorePlayerText.setText("Your Score:" + str(playerScore))
        elif (self.rndcomputer == 1 and self.rndplayer == 3) or (self.rndcomputer == 2 and self.rndplayer == 1) or (

                self.rndcomputer == 3 and self.rndplayer == 2):
            mbox = QMessageBox.information(self, "Information", "Computer wins!")
            computerScore += 1
            self.scorecomputerText.setText("Computer Score:" + str(computerScore))

        if computerScore == 5 or playerScore == 5:
            mbox = QMessageBox.information(self, "Information", "Game Over")
            sys.exit()


def main():
    App = QApplication(sys.argv)
    window = Windows()

    sys.exit(App.exec_())


if __name__ == '__main__':
    main()

