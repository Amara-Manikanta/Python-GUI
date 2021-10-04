import os.path
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize , Qt,QTimer
from PyQt5.QtGui import QIcon
import random,time
from pygame import mixer
from mutagen.mp3 import MP3

musiclist=[]
mixer.init()
muted=False
count = 0
songlength =0
index =0

def groupboxstyle():
    return """
        QGroupBox { 
        background-color:#fcc324;
        font:15pt Times Bold;
        color:white;
        border:2px solid gray;
        border-radius:15px;
        }
    
    """
def progressbar():
    return """
        QProgressBar {
            border: 1px solid #bb;
            background:white;
            height:10px;
            border-radius:15px;
        }
    
    
    """

def playstylesheet():
    return """
        QListWidget{
           background-color:#fff;
           border-radius:10px;
           border:3px solid blue;
        }
    
    """

class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Music Player')
        self.setGeometry(450,150,480,700)
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        ################## Progress Bar
        self.progressbar =QProgressBar()
        self.progressbar.setTextVisible(False)
        self.progressbar.setStyleSheet(progressbar())
        #################################### Labels
        self.songtimelabel =QLabel("0:00")
        self.songlengthlabel =QLabel("/0:00")


        ##################Buttons        ##################
        self.addbutton =QToolButton()
        self.addbutton.setIcon(QIcon('Icons/add.png'))
        self.addbutton.setIconSize(QSize(48,48))
        self.addbutton.setToolTip('Add a song')
        self.addbutton.clicked.connect(self.addsongs)


        self.shufflebutton =QToolButton()
        self.shufflebutton.setIcon(QIcon('Icons/shuffle.png'))
        self.shufflebutton.setIconSize(QSize(48, 48))
        self.shufflebutton.setToolTip('Shuffle the list')
        self.shufflebutton.clicked.connect(self.shufflesongs)

        self.playbutton = QToolButton()
        self.playbutton.setIcon(QIcon('Icons/play.png'))
        self.playbutton.setIconSize(QSize(64, 64))
        self.playbutton.setToolTip('Play')
        self.playbutton.clicked.connect(self.playsong)


        self.prevbutton = QToolButton()
        self.prevbutton.setIcon(QIcon('Icons/previous.png'))
        self.prevbutton.setIconSize(QSize(48, 48))
        self.prevbutton.setToolTip('Play previous song')
        self.prevbutton.clicked.connect(self.prevsong)



        self.nextbutton = QToolButton()
        self.nextbutton.setIcon(QIcon('Icons/next.png'))
        self.nextbutton.setIconSize(QSize(48, 48))
        self.nextbutton.setToolTip('Play Next song')
        self.nextbutton.clicked.connect(self.nextsong)

        self.mutebutton = QToolButton()
        self.mutebutton.setIcon(QIcon('Icons/mute.png'))
        self.mutebutton.setIconSize(QSize(24, 24))
        self.mutebutton.setToolTip('Mute')
        self.mutebutton.clicked.connect(self.mute)

        #############################    Volume Slider

        self.volumeslider = QSlider(Qt.Horizontal)
        self.volumeslider.setToolTip("Volume")
        self.volumeslider.setValue(70)
        self.volumeslider.setMinimum(0)
        self.volumeslider.setMaximum(100)
        mixer.music.set_volume(0.7)
        self.volumeslider.valueChanged.connect(self.setvolume)


        ############################## Play List

        self.playlist =QListWidget()
        self.playlist.doubleClicked.connect(self.playsong)
        self.playlist.setStyleSheet(playstylesheet())

        ############################# Timer
        self.timer=QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updateprogressbar)



    def layouts(self):
        ##################Creating Layouts
        self.mainlayout =QVBoxLayout()
        self.topmainlayout=QVBoxLayout()
        self.topgroupbox =QGroupBox("Music Player")
        self.setStyleSheet(groupboxstyle())
        self.toplayout =QHBoxLayout()
        self.middlelayout = QHBoxLayout()
        self.bottomlayout = QVBoxLayout()

        #############################Adding Widgets######################

        ############################Top Layout Widget####################

        self.toplayout.addWidget(self.progressbar)
        self.toplayout.addWidget(self.songtimelabel)
        self.toplayout.addWidget(self.songlengthlabel)
        #########################   MIddle Layout Widgets
        self.middlelayout.addStretch()

        self.middlelayout.addWidget(self.addbutton)
        self.middlelayout.addWidget(self.shufflebutton)
        self.middlelayout.addWidget(self.playbutton)
        self.middlelayout.addWidget(self.prevbutton)
        self.middlelayout.addWidget(self.nextbutton)
        self.middlelayout.addWidget(self.volumeslider)
        self.middlelayout.addWidget(self.mutebutton)

        self.middlelayout.addStretch()

        ############################# Bottom layout widget

        self.bottomlayout.addWidget(self.playlist)

        self.topmainlayout.addLayout(self.toplayout)
        self.topmainlayout.addLayout(self.middlelayout)

        self.topgroupbox.setLayout(self.topmainlayout)
        self.mainlayout.addWidget(self.topgroupbox,25)
        self.mainlayout.addLayout(self.bottomlayout,75)
        self.setLayout(self.mainlayout)

    def addsongs(self):
        directory =QFileDialog.getOpenFileName(self,'Add song','','Sound files (*.mp3 *.ogg *.wav)')
        #print(directory)
        filename=os.path.basename(directory[0])
        self.playlist.addItem(filename)
        musiclist.append(directory[0])

    def shufflesongs(self):
        random.shuffle(musiclist)
        self.playlist.clear()

        for song in musiclist:
            self.playlist.addItem(os.path.basename(song))

    def playsong(self):
        global songlength,count,index
        count = 0
        index =self.playlist.currentRow()

        try:
            mixer.music.load(str(musiclist[index]))
            mixer.music.play()
            self.timer.start()
            song =MP3(str(musiclist[index]))
            songlength=round(song.info.length)
            min,sec =divmod(songlength,60)
            self.songlengthlabel.setText("/ " + str(min) + ":" + str(sec))
            self.progressbar.setValue(0)
            self.progressbar.setMaximum(songlength)
        except:
            pass


    def setvolume(self):
        self.volume = self.volumeslider.value()
        mixer.music.set_volume(self.volume/100)

    def mute(self):
        global muted

        if muted ==False:
            mixer.music.set_volume(0.0)
            muted =True
            self.mutebutton.setIcon(QIcon('Icons/unmuted.png'))
            self.mutebutton.setToolTip("UnMute")
            self.volumeslider.setValue(0)
        else:
            mixer.music.set_volume(0.7)
            muted = False
            self.mutebutton.setIcon(QIcon('Icons/mute.png'))
            self.mutebutton.setToolTip("Mute")
            self.volumeslider.setValue(self.volume)

    def updateprogressbar(self):
        global count,songlength
        count +=1
        self.progressbar.setValue(count)
        self.songtimelabel.setText(time.strftime("%M:%S",time.gmtime(count)))
        if count ==songlength:
            self.timer.stop()


    def prevsong(self):
        global songlength, count, index
        count = 0
        items =self.playlist.count()
        if index ==0:
            index=items

        index -=1

        try:
            mixer.music.load(str(musiclist[index]))
            mixer.music.play()
            self.timer.start()
            song = MP3(str(musiclist[index]))
            songlength = round(song.info.length)
            min, sec = divmod(songlength, 60)
            self.songlengthlabel.setText("/ " + str(min) + ":" + str(sec))
            self.progressbar.setValue(0)
            self.progressbar.setMaximum(songlength)
        except:
            pass

    def nextsong(self):
        global songlength, count, index
        count = 0
        index += 1
        items = self.playlist.count()
        if index == items:
            index = 0



        try:
            mixer.music.load(str(musiclist[index]))
            mixer.music.play()
            self.timer.start()
            song = MP3(str(musiclist[index]))
            songlength = round(song.info.length)
            min, sec = divmod(songlength, 60)
            self.songlengthlabel.setText("/ " + str(min) + ":" + str(sec))
            self.progressbar.setValue(0)
            self.progressbar.setMaximum(songlength)
        except:
            pass

def main():
    app =QApplication(sys.argv)
    windows=Player()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()