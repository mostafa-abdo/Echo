import sys
import os
from PyQt5.QtCore import Qt, QPoint, QSize
from PyQt5.QtGui import QFontDatabase, QCursor, QColor, QPixmap

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QHBoxLayout, QPushButton, QStackedLayout, QTabWidget,
    QLabel, QGraphicsDropShadowEffect
)


import echo, home, iconButton

class Nav(QWidget):
    def __init__(self,main):
        super().__init__()
        self.navlayout = QHBoxLayout()
        self.navlayout.setAlignment(Qt.AlignTop)
        self.navlayout.setSpacing(0)
        self.navlayout.setContentsMargins(0, 0, 0, 0)

        self.profile = QWidget()
        self.profile.setObjectName('Profile')
        self.profile.setFixedWidth(150)
        self.profile.setFixedHeight(150)
        self.navlayout.addWidget(self.profile)


        profileLayout = QVBoxLayout()
        profileLayout.setAlignment(Qt.AlignTop)
        profileLayout.setContentsMargins(35,0,0,0)
        profileLayout.setSpacing(0)
        self.profile.setLayout(profileLayout)

        self.settings = QPushButton()
        self.settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings.setObjectName('settings')
        self.settings.setFixedWidth(100)
        self.settings.setFixedHeight(30)

        setLayout = QHBoxLayout()
        setLayout.setContentsMargins(0,0,0,0)
        setLayout.setSpacing(5)
        setLayout.setAlignment(Qt.AlignCenter)

        self.settings.setLayout(setLayout)

        self.setlabel = QLabel("Echo")
        self.setlabel.setObjectName('setlabel')

        setLayout.addWidget(self.setlabel)

        self.seti = QLabel()
        setimg = QPixmap('images\\tabs\\angle-down-solid.svg')
        self.seti.setPixmap(setimg.scaled(15,15))
        setLayout.addWidget(self.seti)
        
        profileLayout.addWidget(self.settings)






        self.prof = QWidget()
        self.prof.setObjectName('prof')
        self.prof.setFixedWidth(150)
        self.prof.setContentsMargins(0,0,0,0)
        self.prof.setFixedHeight(90)

        # profileLayout.addWidget(self.prof)

        profLayout = QHBoxLayout()
        profLayout.setContentsMargins(0,0,0,0)
        profLayout.setSpacing(30)
        profLayout.setAlignment(Qt.AlignLeft)

        # self.prof.setLayout(profLayout)

        self.profi = QLabel()
        self.profi.setCursor(QCursor(Qt.PointingHandCursor))
        profimg = QPixmap('images\\profile_img\\pc1.png')
        self.profi.setPixmap(profimg.scaled(60,60))

        # profLayout.addWidget(self.profi)



        self.bell = QLabel()
        self.bell.setCursor(QCursor(Qt.PointingHandCursor))
        bellimg = QPixmap('images\\tabs\\bell-regular.svg')
        self.bell.setPixmap(bellimg.scaled(25,30))

        # profLayout.addWidget(self.bell)
        



        self.tabs = QWidget()
        self.tabs.setObjectName('Tabs')
        self.tabs.setContentsMargins(300,0,340,0)
        self.navlayout.addWidget(self.tabs)


        tabsLayout = QHBoxLayout()
        tabsLayout.setSpacing(0)
        tabsLayout.setContentsMargins(0,0,0,0)
        


        self.homeTab =  iconButton.IconButton("images\\tabs\house-solid.svg", "images\\tabs\house-light.svg","HOME", 45, 40, 70, 70)   
        self.homeTab.clicked.connect(main.show_home)

        tabsLayout.addWidget(self.homeTab)


        self.devTab =  iconButton.IconButton("images\\tabs\devices-solid.svg", "images\\tabs\devices-light.svg","DEVICES", 50, 40, 70, 70)
        self.devTab.clicked.connect(main.show_devices)

        tabsLayout.addWidget(self.devTab)


        self.finTab =  iconButton.IconButton("images\\tabs\download-solid.svg", "images\\tabs\download-light.svg","FINISHED", 40, 40, 70, 70)
        self.finTab.clicked.connect(main.show_finished)
        tabsLayout.addWidget(self.finTab)
    
    
        self.statusTab =  iconButton.IconButton("images\\tabs\wifi-solid.svg", "images\\tabs\wifi-light.svg","STATUS", 60, 40, 70, 70)

        tabsLayout.addWidget(self.statusTab)

        self.tabs.setLayout(tabsLayout)


        self.homeTab.clicked.connect(lambda: self.disactive(0))
        self.devTab.clicked.connect(lambda: self.disactive(1))
        self.finTab.clicked.connect(lambda: self.disactive(2))
        self.statusTab.clicked.connect(lambda: self.disactive(3))




        self.exitbar = QWidget()
        self.exitbar.setObjectName('exitBar')
        self.exitbar.setContentsMargins(0,0,0,0)

        self.exitbar.setFixedWidth(110)
        self.exitbar.setFixedHeight(150)
        self.navlayout.addWidget(self.exitbar)

        self.exitbarLayout = QHBoxLayout()
        self.exitbarLayout.setSpacing(0)
        self.exitbarLayout.setContentsMargins(20,20,0,0)
        self.exitbarLayout.setSpacing(15)
        self.exitbarLayout.setAlignment(Qt.AlignTop)

        self.exitbtn = QPushButton('')
        self.exitbtn.setObjectName('Exitbtn')
        self.exitbtn.clicked.connect(main.close)
        self.exitbtn.setFixedHeight(16)
        self.exitbtn.setFixedWidth(16)
        self.exitbtn.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.minbtn = QPushButton('')
        self.minbtn.setObjectName('Minbtn')
        self.minbtn.clicked.connect(main.showNormal)
        self.minbtn.setFixedHeight(16)
        self.minbtn.setFixedWidth(16)
        self.minbtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.hidebtn = QPushButton('')
        self.hidebtn.setObjectName('Hidebtn')
        self.hidebtn.clicked.connect(main.showMinimized)
        self.hidebtn.setFixedHeight(16)
        self.hidebtn.setFixedWidth(16)
        self.hidebtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.exitbarLayout.addWidget(self.hidebtn)
        self.exitbarLayout.addWidget(self.minbtn)
        self.exitbarLayout.addWidget(self.exitbtn)

        self.exitbar.setLayout(self.exitbarLayout)


    def disactive(self, num = 0):
        self.homeTab.disactive()
        self.devTab.disactive()
        self.finTab.disactive()
        self.statusTab.disactive()

        if num == 0:
            self.homeTab.active()
        elif num == 1:
            self.devTab.active()
        elif num == 2:
            self.finTab.active()
        elif num == 3:
            self.statusTab.active()
