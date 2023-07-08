import sys
import os
from PyQt5.QtCore import Qt, QPoint, QSize
from PyQt5.QtGui import QFontDatabase, QCursor, QColor, QPixmap

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QHBoxLayout, QPushButton, QStackedLayout, QTabWidget,
    QLabel, QGraphicsDropShadowEffect, QTableWidget
)

from table import Table
from cardInfo import CardInfo
from appInfo import AppInfo

class Home(QWidget):
    def __init__(self,width,height):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.HomeLayout = QVBoxLayout()
        self.HomeLayout.setAlignment(Qt.AlignTop)
        self.HomeLayout.setSpacing(0)
        self.HomeLayout.setContentsMargins(0, 0, 0, 0)

        styleFile=os.path.join(os.path.split(__file__)[0],"stylesheet\home.qss")
        styleSheetStr = open(styleFile,"r").read()
        self.setStyleSheet(styleSheetStr)

        self.sInfo = QWidget()
      
        self.sInfo.setMinimumWidth(width)
        self.sInfo.setFixedHeight(320)
        
        self.infoLayout = QHBoxLayout()
        self.infoLayout.addWidget(CardInfo(0, "PC1", "00:2D:55:DD:FD:EE", "192.168.1.2","images\\profile_img\\pc1.png"))

        

        self.sPInfo = AppInfo()
        


        self.infoLayout.addWidget(self.sPInfo)

        self.infoLayout.addWidget(CardInfo(1, "PC2", "00:2D:55:DD:FD:E1", "192.168.1.3","images\\profile_img\\pc2.png"))

        self.sInfo.setLayout(self.infoLayout)
        

        self.sTable = QWidget()
        self.sTable.setStyleSheet("")
        
        self.sTable.setMinimumWidth(width)
        
        self.sTable.setFixedHeight(320)


        self.tableLayout = QHBoxLayout()
        self.tableLayout.setContentsMargins(0, 0, 0, 0)
        self.tableLayout.setSpacing(0)
        self.tableLayout.setAlignment(Qt.AlignLeft)

        self.sPs = QWidget()
        self.sPs.setStyleSheet("")
        self.sPs.setFixedWidth(410)
        
        pbtn = QPushButton()
        pbtn.setFixedSize(150, 150)
        pbtn.setCursor(QCursor(Qt.PointingHandCursor))
        pbtn.setStyleSheet("""
            background-color: #64ca57;
            border-radius: 75px;
            font-size: 50px;
            color: #ffffff;
        """)
        pimg = QPixmap("images\\pause-solid.svg")

        pimage = QLabel()
        pimage.setStyleSheet("")
        pimage.setFixedSize(60,70)
        pimage.setPixmap(pimg.scaled(60,70))
        pimage.setAlignment(Qt.AlignCenter)

        pbtnilayout = QHBoxLayout()
        pbtnilayout.setSpacing(0)
        pbtnilayout.setContentsMargins(0,0,0,0)
        pbtnilayout.addWidget(pimage)

        pbtn.setLayout(pbtnilayout)

        pbtnlayout = QHBoxLayout()
        pbtnlayout.setSpacing(0)
        pbtnlayout.setContentsMargins(0,0,0,0)

        pbtnlayout.addWidget(pbtn)

        self.sPs.setLayout(pbtnlayout)
       
        self.tableLayout.addWidget(self.sPs)

        
        
        heads = ["STATUS", "RECEIVER", "RECEIVER MAC", "RECEIVER IP", "PROGRESS"]
        types = [0, 1, 2, 2, 3]
        sizes = [100, 200, 200 , 200, 200]
        data = [
            [1,["images\\profile_img\\pc1.png", "PC1"], "AA:BB:CC:DD:EE:FF", "123.456.789.100", 50]
        ]
        
        self.table = Table(15, 5, 950, 300, heads, types, sizes, data)
        

        

        self.sTInfo = QWidget()

        tlay = QHBoxLayout()
        tlay.setContentsMargins(0,0,0,0)
        tlay.addWidget(self.table)
        self.sTInfo.setLayout(tlay)
        self.sTInfo.setStyleSheet("background-color: #232339;")
        
        self.sTInfo.setFixedSize(960, 300)
        self.tableLayout.addWidget(self.sTInfo)

        

        self.sTable.setLayout(self.tableLayout)
        
    


        self.HomeLayout.addWidget(self.sInfo)
        self.HomeLayout.addWidget(self.sTable)
        self.setLayout(self.HomeLayout)