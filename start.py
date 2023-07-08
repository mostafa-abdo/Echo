import sys
import os
from PyQt5.QtCore import Qt, QPoint, QSize
from PyQt5.QtGui import QFontDatabase, QCursor, QColor, QPixmap

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QHBoxLayout, QPushButton, QStackedLayout, QTabWidget,
    QLabel, QGraphicsDropShadowEffect
)

class Start(QWidget):
     def __init__(self, width, height):
        super().__init__()
        startlayout = QHBoxLayout()

        self.startbtn = QPushButton("Echo")
        self.startbtn.setObjectName('Echobtn')
        self.startbtn.setFixedHeight(300)
        self.startbtn.setFixedWidth(300)
        self.startbtn.setCursor(QCursor(Qt.PointingHandCursor))
        
        
        self.startbtnshadow = QGraphicsDropShadowEffect()
        self.startbtnshadow.setBlurRadius(25)
        self.startbtnshadow.setColor(QColor(220, 220, 246).lighter())
        self.startbtnshadow.setOffset(0)
    

        self.startbtn.setGraphicsEffect(self.startbtnshadow)
    
        startlayout.addWidget(self.startbtn)
        self.setLayout(startlayout)


