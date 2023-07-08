import sys
import os
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QCursor, QColor, QPixmap

from PyQt5.QtWidgets import (
    QVBoxLayout, QWidget,
    QHBoxLayout, QPushButton, QStackedLayout,
    QLabel, QScrollArea, QScrollBar
)

from table import Table
from itemlist import ItemList


class Finished(QWidget):
    def __init__(self,width,height):
        super().__init__()
        self.setContentsMargins(0,0,0,0)

        
        self.DevicesLayout = QVBoxLayout()
        self.DevicesLayout.setAlignment(Qt.AlignCenter)
        self.DevicesLayout.setContentsMargins(60, 60, 60, 0)
        self.DevicesLayout.setSpacing(0)

        styleFile=os.path.join(os.path.split(__file__)[0],"stylesheet\home.qss")
        styleSheetStr = open(styleFile,"r").read()
        self.setStyleSheet(styleSheetStr)

        
        heads = ["checkbox-1", "SENDER","RECEIVER", "SOFTWARE", "DATE", "REMOVE"]
        types = [4, 1, 1, 1, 2, 5]
        sizes = [50, 200, 200, 200 , 200, 80]
        data = [
            [1, ["images\\profile_img\\pc1.png", "PC1"], ["images\\profile_img\\pc1.png", "PC1"], ["images\\photoshop.png", "Photoshop"], "12:00 AM / 1 DES 2022", 1],
            [1, ["images\\profile_img\\pc1.png", "PC1"], ["images\\profile_img\\pc1.png", "PC1"], ["images\\photoshop.png", "Photoshop"], "12:00 AM / 1 DES 2022", 1],
            [1, ["images\\profile_img\\pc1.png", "PC1"], ["images\\profile_img\\pc1.png", "PC1"], ["images\\photoshop.png", "Photoshop"], "12:00 AM / 1 DES 2022", 1]
        ]
        
        self.table = Table(15, 6, 960, 500, heads, types, sizes, data)
        self.table.setStyleSheet("")

        self.tablewid = QWidget()
        self.tablewid.setContentsMargins(0, 0, 0, 0)

        self.tablewidlayout = QHBoxLayout()
        self.tablewid.setLayout(self.tablewidlayout)
        

        self.tablewidlayout.addWidget(self.table)
        self.tablewidlayout.setAlignment(Qt.AlignCenter)
        self.tablewidlayout.setContentsMargins(0, 0, 0, 0)
        self.tablewidlayout.setSpacing(40)

        self.list = ItemList()
        items = [
            ['images/photoshop.png', 'Photoshop2021'],
            ['images/photoshop.png', 'Photoshop2022'],
            ['images/photoshop.png', 'Photoshop2023'],
            ]
        self.list.addListitems(items=items)
        self.tablewidlayout.addWidget(self.list)


        self.DevicesLayout.addWidget(self.tablewid)




        self.options = QWidget()
        self.options.setFixedHeight(120)
        self.options.setStyleSheet("back")

        optlayout = QHBoxLayout()
        optlayout.setSpacing(0)
        optlayout.setContentsMargins(0, 0, 0, 0)
        optlayout.setAlignment(Qt.AlignLeft)
        self.options.setLayout(optlayout)

        removebtn = QPushButton('REMOVE SELECTED')
        removebtn.setCursor(QCursor(Qt.PointingHandCursor))
        removebtn.setFixedSize(200, 50)
        removebtn.setStyleSheet(
            "background-color: #ed6b60;"
            "color: #232339;"
            "font-size: 22px;"
            "font-weight: bold;"
            "font-family: Agency FB;"
            "border:none;"
            "border-radius: 10px;"
        )
        optlayout.addWidget(removebtn)



        self.DevicesLayout.addWidget(self.options)
        
        


        self.setLayout(self.DevicesLayout)