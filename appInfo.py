import sys
import os
from PyQt5.QtCore import Qt, QPoint, QSize
from PyQt5.QtGui import QFontDatabase, QCursor, QColor, QPixmap, QTransform, QImage, QPainter

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QHBoxLayout, QPushButton, QStackedLayout, QTabWidget,
    QLabel, QGraphicsDropShadowEffect, QTableWidget
)



class AppInfo(QWidget):
    def __init__(self, appName = "", appImage = "", appSize = ""):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.setFixedSize(600,200)
        self.setStyleSheet("color: #dcdcf6;")
        
        aimg = QPixmap("images\\photoshop.png")

        
        self.appimage = QLabel()
        self.appimage.setPixmap(aimg.scaled(100,100))
        self.appimage.setAlignment(Qt.AlignCenter)

        
        
        self.img = QWidget()
        self.img.setStyleSheet('')
        self.img.setFixedSize(120,120)

        imgl = QVBoxLayout()
        imgl.addWidget(self.appimage)

        self.img.setLayout(imgl)
        

        self.info = QWidget()
        self.info.setStyleSheet('')

        infol = QVBoxLayout()

        appname = QLabel("Photoshop")
        appname.setStyleSheet("font-size: 25px;font-weight: bold;font-family: 'Agency FB';")

        appsize = QLabel("Size: 100Mb")
        appsize.setStyleSheet("font-size:12px;font-family:Arial;")

        downprog = QWidget()
        downprog.setStyleSheet("background-color:#484867;border:1px solid #7d7d9a;border-radius:5px;")
        downprog.setFixedSize(400,15)

        dpl = QVBoxLayout()
        dpl.setContentsMargins(0,0,0,0)
        dpl.setSpacing(0)

        idp = QWidget()
        idp.setStyleSheet("background-color: #64ca57;")
        idp.setFixedSize(400,15)

        dpl.addWidget(idp)

        downprog.setLayout(dpl)

        downlabel = QLabel("Downloaded...... 100%")
        downlabel.setStyleSheet("font-size:12px;font-family:Arial;")

        instprog = QWidget()
        instprog.setStyleSheet("background-color:#484867;border:1px solid #7d7d9a;border-radius:5px;")
        instprog.setFixedSize(400,15)

        ipl = QVBoxLayout()
        ipl.setContentsMargins(170,0,0,0)
        ipl.setSpacing(0)

        iip = QWidget()
        iip.setStyleSheet("background-color: #ed6b60;")
        iip.setFixedSize(60,15)

        ipl.addWidget(iip)

        instprog.setLayout(ipl)

        instlabel = QLabel("Installing......")
        instlabel.setStyleSheet("font-size:12px;font-family:Arial;")
        

        infol.addWidget(appname)
        infol.addWidget(appsize)
        infol.addWidget(downprog)
        infol.addWidget(downlabel)
        infol.addWidget(instprog)
        infol.addWidget(instlabel)


        self.info.setLayout(infol)
        

        self.ilay = QHBoxLayout()

        self.ilay.addWidget(self.img) 
        self.ilay.addWidget(self.info) 

        self.setLayout(self.ilay)

        

        