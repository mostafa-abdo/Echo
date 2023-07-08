from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QStackedLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap, QColor, QCursor
from PyQt5.QtCore import Qt
import sys

class IconButton(QPushButton):
    def __init__(self, svgimg = "", asvg="", label = "TEST",imgwidth = 40, imgheight = 40, btnwidth = 80, btnheight = 80):
        super().__init__()
        self.setFixedSize(btnwidth, btnheight)
        self.setStyleSheet("background-color:transparent;")
        self.btnclicked = False

        self.btnlayout = QVBoxLayout()
        self.btnlayout.setContentsMargins(0,0,0,0)
        self.btnlayout.setSpacing(0)
        self.btnlayout.setAlignment(Qt.AlignCenter)

        icon = QWidget()
        icon.setStyleSheet("")
        icon.setContentsMargins(0,0,0,0)


        self.buttonlayout = QStackedLayout()

        self.svg = QPixmap(svgimg)

        icon1 = QLabel()
        icon1.setPixmap(self.svg.scaled(imgwidth, imgheight))
        icon1.setAlignment(Qt.AlignCenter)

        self.svg = QPixmap(asvg)

        icon2 = QLabel()
        icon2.setPixmap(self.svg.scaled(imgwidth, imgheight))
        icon2.setAlignment(Qt.AlignCenter)

        
        self.buttonlayout.addWidget(icon1)
        self.buttonlayout.addWidget(icon2)

        icon.setLayout(self.buttonlayout)

        self.label = QLabel(label)
        self.label.setStyleSheet("""
            font-size: 18px;
            color: #232339;
            font-family: 'Agency FB', sans-serif;
            font-weight: bold;
        """)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setContentsMargins(0,0,0,0)

        self.btnlayout.addWidget(icon)
        self.btnlayout.addWidget(self.label)

        self.setLayout(self.btnlayout)
        self.setCursor(QCursor(Qt.PointingHandCursor))

        self.clicked.connect(self.active)

    def active(self):
        self.buttonlayout.setCurrentIndex(1)
        self.label.setStyleSheet("""
            font-size: 18px;
            color: #e4e4f8;
            font-family: 'Agency FB', sans-serif;
            font-weight: bold;
        """)
        self.btnclicked = True

    def disactive(self):
        self.buttonlayout.setCurrentIndex(0)
        self.label.setStyleSheet("""
            font-size: 18px;
            color: #232339;
            font-family: 'Agency FB', sans-serif;
            font-weight: bold;
        """)
        self.btnclicked = False

    def enterEvent(self, event):
        self.buttonlayout.setCurrentIndex(1)
        self.label.setStyleSheet("""
            font-size: 18px;
            color: #e4e4f8;
            font-family: 'Agency FB', sans-serif;
            font-weight: bold;
        """)


    def leaveEvent(self, event):
        if not self.btnclicked:
            self.buttonlayout.setCurrentIndex(0)
            self.label.setStyleSheet("""
                font-size: 18px;
                color: #232339;
                font-family: 'Agency FB', sans-serif;
                font-weight: bold;
            """)

        



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainlayout = QHBoxLayout()
        
        self.button = IconButton("images\\tabs\house-solid.svg", "images\\tabs\house-light.svg","HOME", 40, 40, 80, 80)
        self.button1 = IconButton("images\\tabs\house-solid.svg", "images\\tabs\house-light.svg","HOME", 40, 40, 80, 80)
        self.button2 = IconButton("images\\tabs\house-solid.svg", "images\\tabs\house-light.svg","HOME", 40, 40, 80, 80)

        self.button.clicked.connect(lambda: self.disactive(0))
        self.button1.clicked.connect(lambda: self.disactive(1))
        self.button2.clicked.connect(lambda: self.disactive(2))

        mainlayout.addWidget(self.button)
        mainlayout.addWidget(self.button1)
        mainlayout.addWidget(self.button2)

        self.setLayout(mainlayout)

    def disactive(self, num = 0):
        self.button.disactive()
        self.button1.disactive()
        self.button2.disactive()

        if num == 0:
            self.button.active()
        elif num == 1:
            self.button1.active()
        elif num == 2:
            self.button2.active()
        


# if __name__ == "__main__":
#     app = QApplication([])
#     ex = MainWindow()
#     ex.show()
#     sys.exit(app.exec_())
