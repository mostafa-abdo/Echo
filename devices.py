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

class Devices(QWidget):
    def __init__(self,width,height):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.DevicesLayout = QHBoxLayout()
        self.DevicesLayout.setAlignment(Qt.AlignCenter)
        self.DevicesLayout.setSpacing(0)
        self.DevicesLayout.setContentsMargins(60, 60, 0, 0)

        styleFile=os.path.join(os.path.split(__file__)[0],"stylesheet\home.qss")
        styleSheetStr = open(styleFile,"r").read()
        self.setStyleSheet(styleSheetStr)

        
        heads = ["STATUS", "SENDER","RECEIVER", "RECEIVER MAC", "RECEIVER IP", "PROGRESS"]
        types = [0, 1, 1, 2, 2, 3]
        sizes = [100, 200, 200, 200 , 200, 200]
        data = [
            [1, ["images\\profile_img\\pc1.png", "PC1"], ["images\\profile_img\\pc1.png", "PC1"], "AA:BB:CC:DD:EE:FF", "123.456.789.100", 50]
        ]
        
        self.table = Table(15, 6, 1280, 560, heads, types, sizes, data)

        

        self.DevicesLayout.addWidget(self.table)
        
        


        self.setLayout(self.DevicesLayout)