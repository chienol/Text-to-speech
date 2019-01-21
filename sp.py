#!usr/bin/python3 
  

#chuong trinh dc viet boi Bui Minh Chien (0xcd80 )

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
import os

lg=sys.argv[1]

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(500, 350))
        self.setWindowTitle("phần mềm chuyển chữ sang giọng nói ")

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('text')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(300, 100)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('nói ', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(100, 150)


    def clickMethod(self):
        from tqdm import tqdm
        import requests
        import os
        import subprocess

        def play(path):
            subprocess.Popen(['mpg123', '-q', path]).wait()


        url ='https://translate.google.com.vn/translate_tts?ie=UTF-8&q=' + self.line.text() + """&tl="""+lg+"""&client=tw-ob"""
        response = requests.get(url, stream=True)

        with open("10MB.mp3", "wb") as handle:
            for data in tqdm(response.iter_content()):
                handle.write(data)

        play("10MB.mp3")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
