import sys
import os
from PyQt5.QtCore import Qt, QPoint, QSize
from PyQt5.QtGui import QFontDatabase, QCursor, QColor, QPixmap

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QHBoxLayout, QPushButton, QStackedLayout, QTabWidget,
    QLabel, QGraphicsDropShadowEffect, QTableWidget
)



class CardInfo(QWidget):
    def __init__(self,type=0, name="", mac="", ip="", img=""):
        super().__init__()

        
        self.setFixedSize(360, 210)
        self.setStyleSheet("""
            background-color:#8e8eb3;
            border-top-left-radius: 10px;
            border-bottom-left-radius: 10px;
            border-top-right-radius: 10px;
            border-bottom-right-radius: 10px;
        """)
       
        
        self.senderLayout = QVBoxLayout()
        self.senderLayout.setContentsMargins(0,0,0,0)
        self.senderLayout.setSpacing(0)
        self.senderLayout.setAlignment(Qt.AlignVCenter)
        self.senderLayout.setAlignment(Qt.AlignTop)
        

        self.sTitle = QWidget()
        self.sTitle.setStyleSheet("")

        

        self.sTitleLayout = QVBoxLayout()
        self.sTitleLayout.setContentsMargins(0,0,0,0)
        self.sTitleLayout.setSpacing(0)
        self.sTitleLayout.setAlignment(Qt.AlignTop)
        
        if type == 0 :
            self.sTitleText = QLabel("SENDER")
        else:
            self.sTitleText = QLabel("RECEIVER")
        self.sTitleText.setFixedHeight(60)
        self.sTitleText.setAlignment(Qt.AlignHCenter)
        self.sTitleText.setStyleSheet("""
            color:#fff;
            font-size:30px;
            font-family:Cairo;
            font-weight:bold;
            border-bottom-left-radius: 0px;
            border-bottom-right-radius: 0px;
        """)
        self.sTitleLayout.addWidget(self.sTitleText)

        self.sTitle.setLayout(self.sTitleLayout)

        self.senderInfo = QWidget()
        self.senderInfo.setStyleSheet('''
            border-top-left-radius: 0px;
            border-top-right-radius: 0px;
        ''')
        self.senderInfo.setFixedHeight(150)
        

        self.senderInfoLayout = QHBoxLayout()
        self.senderInfoLayout.setAlignment(Qt.AlignVCenter)
        self.senderInfoLayout.setContentsMargins(20,0,0,0)

        self.senderImage = QWidget()
        self.senderImage.setFixedSize(80,80)
        self.senderImage.setStyleSheet('''
            background-color:red;
            border-top-left-radius: 40px;
            border-bottom-left-radius: 40px;
            border-top-right-radius: 40px;
            border-bottom-right-radius: 40px;'''
        )

        self.ci = QLabel()
        self.ci.setFixedSize(80,80)
        self.ci.setCursor(QCursor(Qt.PointingHandCursor))
        cimg = QPixmap(img)
        self.ci.setPixmap(cimg.scaled(80,80))


        self.senderI = QWidget()

        self.senderILayout = QVBoxLayout()
        self.senderILayout.setSpacing(10)

        self.sName = QWidget()

        self.sNameT = QLabel('NAME:')
        self.sNameT.setStyleSheet("color: #232339;font-size:18px;font-weight:bold;font-family:Arial;")
        
        self.sNameV = QLabel(name)
        self.sNameV.setStyleSheet("color: #fff;font-size:16px;font-family:Arial;")

        sNameLayout = QHBoxLayout()
        sNameLayout.setContentsMargins(0,0,0,0)
        sNameLayout.setSpacing(15)
        sNameLayout.setAlignment(Qt.AlignLeft)
        sNameLayout.addWidget(self.sNameT)
        sNameLayout.addWidget(self.sNameV)

        self.sName.setLayout(sNameLayout)



        self.sMac = QWidget()

        self.sMacT = QLabel('MAC:')
        self.sMacT.setStyleSheet("color: #232339;font-size:18px;font-weight:bold;font-family:Arial;")
        
        self.sMacV = QLabel(mac)
        self.sMacV.setStyleSheet("color: #fff;font-size:16px;font-family:Arial;")

        sMacLayout = QHBoxLayout()
        sMacLayout.setContentsMargins(0,0,0,0)
        sMacLayout.setSpacing(10)
        sMacLayout.setAlignment(Qt.AlignLeft)
        sMacLayout.addWidget(self.sMacT)
        sMacLayout.addWidget(self.sMacV)

        self.sMac.setLayout(sMacLayout)


        self.sIP = QWidget()

        self.sIPT = QLabel('IP:')
        self.sIPT.setStyleSheet("color: #232339;font-size:18px;font-weight:bold;font-family:Arial;")
        
        self.sIPV = QLabel(ip)
        self.sIPV.setStyleSheet("color: #fff;font-size:16px;font-family:Arial;")

        sIPLayout = QHBoxLayout()
        sIPLayout.setContentsMargins(0,0,0,0)
        sIPLayout.setSpacing(10)
        sIPLayout.setAlignment(Qt.AlignLeft)
        sIPLayout.addWidget(self.sIPT)
        sIPLayout.addWidget(self.sIPV)

        self.sIP.setLayout(sIPLayout)


        
        
        self.senderILayout.addWidget(self.sName)
        self.senderILayout.addWidget(self.sMac)
        self.senderILayout.addWidget(self.sIP)

        self.senderI.setLayout(self.senderILayout)


        self.senderInfoLayout.addWidget(self.ci)
        self.senderInfoLayout.addWidget(self.senderI)

        self.senderInfo.setLayout(self.senderInfoLayout)
        self.senderLayout.addWidget(self.sTitle)
        self.senderLayout.addWidget(self.senderInfo)
        
        self.setLayout(self.senderLayout)
