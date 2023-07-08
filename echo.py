import sys
import os
from PyQt5.QtCore import Qt, QPoint, QSize
from PyQt5.QtGui import QFontDatabase, QCursor, QColor, QPixmap

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QHBoxLayout, QPushButton, QStackedLayout
)
import start, nav, home, devices, finished, design, waiting

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint )
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setObjectName('MainWindow')
        self.setWindowTitle("Echo")
        self.setGeometry(260, 140, 1400, 800)
        self.setFixedWidth(1400)
        self.setFixedHeight(800)
        self.setContentsMargins(0, 0, 0, 0)
        
        styleFile=os.path.join(os.path.split(__file__)[0],"stylesheet\style.qss")
        styleSheetStr = open(styleFile,"r").read()
        self.setStyleSheet(styleSheetStr) 

        QFontDatabase.addApplicationFont('fonts/Viga-Regular.ttf')
        QFontDatabase.addApplicationFont('fonts/AGENCYB.TTF')

        

        self.body = QWidget()
        self.body.setObjectName('Body')
        self.body.setContentsMargins(0, 0, 0, 0)
        self.body.setAttribute(Qt.WA_TranslucentBackground, True)

        mainLayout = QVBoxLayout()
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        self.navbar = QWidget()
        self.navbar.setObjectName('Nav')
        self.navbar.setFixedHeight(120)
        self.navbar.setContentsMargins(0, 0, 0, 0)
        mainLayout.addWidget(self.navbar)


        
        self.navbar.setLayout(nav.Nav(self).navlayout)

        self.content = QWidget()
        self.content.setStyleSheet("")
        self.content.setObjectName('Content')
        self.content.setContentsMargins(0, 0, 0, 0)

        self.start = start.Start(1400, 800)
        self.start.startbtn.clicked.connect(self.show_design)
        self.waiting = waiting.WaitingWidget()
        # self.design = design.Design()
        self.home = home.Home(1400, 800)
        self.devices = devices.Devices(1400, 800)
        self.finished = finished.Finished(1400, 800)
        

        self.contentLayout = QStackedLayout()
        self.contentLayout.setAlignment(Qt.AlignCenter)

        
        self.contentLayout.addWidget(self.start)
        self.contentLayout.addWidget(self.waiting)
        # self.contentLayout.addWidget(self.design)
        self.contentLayout.addWidget(self.home)
        self.contentLayout.addWidget(self.devices)
        self.contentLayout.addWidget(self.finished)


        self.content.setLayout(self.contentLayout)
        

        self.show_start()

        mainLayout.addWidget(self.content)

        self.body.setLayout(mainLayout)

        self.setCentralWidget(self.body)

        self.body.setLayout(mainLayout)

        self.setCentralWidget(self.body)
    
    def show_start(self):
        self.contentLayout.setCurrentWidget(self.start)

    def show_waiting(self):
        self.contentLayout.setCurrentWidget(self.waiting)

    def show_design(self):
        self.design = design.Design()
        self.contentLayout.addWidget(self.design)
        self.contentLayout.setCurrentWidget(self.design)

    def show_home(self):
        self.contentLayout.setCurrentWidget(self.home)

    def show_devices(self):
        self.contentLayout.setCurrentWidget(self.devices)

    def show_finished(self):
        self.contentLayout.setCurrentWidget(self.finished)








if __name__ == '__main__' :

    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec_()
