import typing
from PyQt5.QtWidgets import QWidget, QListWidget, QListWidgetItem, QScrollBar, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QColor, QCursor


class ItemList(QWidget):
    def __init__(self, width = None, height = None, background = 'transparent', radius = '10px', border = "1px solid #8e8eb3", color = "#dcdcf6"):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)


        title = QWidget()
        title.setFixedHeight(50)
        title.setStyleSheet(
            "QWidget{"
            "   border: 1px solid #8e8eb3;"
            "   background-color: #8e8eb3;"
            "   border-top-right-radius: 10px;"
            "   border-top-left-radius: 10px;"
            "   font-size: 18px;"
            "   font-family: 'Agency FB';"
            "   font-weight: bold;"
            "   color: #dcdcf6;"
            "}"
        )
        
        titlelayout = QVBoxLayout()
        titlelayout.setAlignment(Qt.AlignCenter)

        titlelabel = QLabel("INSTALLED SOFTWARES")
        titlelayout.addWidget(titlelabel)

        title.setLayout(titlelayout)

        layout.addWidget(title)

        self.listwid = QListWidget()
        layout.addWidget(self.listwid)
        if width != None:
            self.listwid.setFixedWidth(width)
        elif height != None:
            self.listwid.setFixedHeight(height)

        self.listwid.setStyleSheet(
            "QListWidget {"
                f"background-color:{background};"
                f"border-radius:{radius};"
                "border-top-left-radius: 0;"
                "border-top-right-radius: 0;"
                f"border: {border};"
                f"color: {color};"
                "padding-bottom: 5px;"
                "font-size: 16px;"
                "background-color: #232339;"
                "alternate-background-color: #484867;"
            "}"
            "QListWidget Item:hover {"
                "background-color: #64ca57;"
            "}"
        )

        scrollbar = QScrollBar(Qt.Vertical)
        self.listwid.setVerticalScrollBar(scrollbar)
        self.listwid.setStyleSheet(self.listwid.styleSheet()+
            "QScrollBar:vertical {"
            "    border: none;"
            "    border-left: 1px solid #8e8eb3;"
            "    border-radius: 10px;"
            "    background-color: transparent;"
            "    width: 15px;"
            "    margin: 0px 0px 0px 0px;"
            "    padding-bottom: 10px;"
            "}"
            "QScrollBar::handle:vertical {"
            "   border:none;"
            "   background-color: #8e8eb3;"
            "   min-height: 50px;"
            "}"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {"
            "    height: 0px;"
            "   border:none;"
            "}"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {"
            "   border:none;"
            "    background: none;"
            "}"
        )
        self.listwid.setIconSize(QSize(30, 30))

    def addListitems(self, items = []):
        for item in items:
            listitem = QListWidgetItem(QIcon(item[0]), item[1])
            listitem.setToolTip(item[1])
            listitem.setSizeHint(QSize(0, 50))
            num = self.listwid.count()
            self.listwid.addItem(listitem)
            if num % 2 != 0:
                self.listwid.item(num).setBackground(QColor('#484867'))

    def addListitem(self, item = []):
        listitem = QListWidgetItem(QIcon(item[0]), item[1])
        listitem.setToolTip(item[1])
        self.listwid.addItem(listitem)



class ItemListPlus(QWidget):
    def __init__(self, width = None, height = None, background = 'transparent', radius = '10px', border = "1px solid #8e8eb3", color = "#dcdcf6"):
        super().__init__()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignLeft)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        content = QWidget()
        

        layout.addWidget(content)


        contentlayout = QVBoxLayout()
        contentlayout.setAlignment(Qt.AlignLeft)
        contentlayout.setSpacing(0)
        contentlayout.setContentsMargins(0, 0, 0, 0)

        content.setLayout(contentlayout)


        title = QWidget()
        title.setFixedHeight(50)
        title.setStyleSheet(
            "QWidget{"
            "   border: 1px solid #8e8eb3;"
            "   background-color: #8e8eb3;"
            "   border-top-right-radius: 10px;"
            "   border-top-left-radius: 10px;"
            "   font-size: 18px;"
            "   font-family: 'Agency FB';"
            "   font-weight: bold;"
            "   color: #dcdcf6;"
            "}"
        )
        
        titlelayout = QVBoxLayout()
        titlelayout.setAlignment(Qt.AlignCenter)

        titlelabel = QLabel("SELECTED SOFTWARES")
        titlelayout.addWidget(titlelabel)

        title.setLayout(titlelayout)

        contentlayout.addWidget(title)

        self.listwid = QListWidget()
        contentlayout.addWidget(self.listwid)
        if width != None:
            self.setFixedWidth(width)
            self.listwid.setFixedWidth(width)
        elif height != None:
            self.setFixedHeight(height)
            self.listwid.setFixedHeight(height)

        self.listwid.setStyleSheet(
            "QListWidget {"
                f"background-color:{background};"
                f"border-radius:0;"
                "border-top-left-radius: 0;"
                "border-top-right-radius: 0;"
                f"border: {border};"
                f"color: {color};"
                "padding-bottom: 5px;"
                "font-size: 16px;"
                "background-color: #232339;"
                "alternate-background-color: #484867;"
            "}"
            "QListWidget Item:hover {"
                "background-color: #64ca57;"
            "}"
        )

        scrollbar = QScrollBar(Qt.Vertical)
        self.listwid.setVerticalScrollBar(scrollbar)
        self.listwid.setStyleSheet(self.listwid.styleSheet()+
            "QScrollBar:vertical {"
            "    border: none;"
            "    border-left: 1px solid #8e8eb3;"
            "    border-radius: 10px;"
            "    background-color: transparent;"
            "    width: 15px;"
            "    margin: 0px 0px 0px 0px;"
            "    padding-bottom: 10px;"
            "}"
            "QScrollBar::handle:vertical {"
            "   border:none;"
            "   background-color: #8e8eb3;"
            "   min-height: 50px;"
            "}"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {"
            "    height: 0px;"
            "   border:none;"
            "}"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {"
            "   border:none;"
            "    background: none;"
            "}"
        )
        self.listwid.setIconSize(QSize(30, 30))

        rmbtnwid = QWidget()
        rmbtnwid.setContentsMargins(0, 0, 0, 0)
        rmbtnwid.setFixedHeight(60)
        rmbtnwid.setStyleSheet(
            "border: 1px solid #8e8eb3;"
            "border-top: none;"
            "border-bottom-right-radius: 10;"
            "border-bottom-left-radius: 10;"
        )

        rmbtnlayout = QVBoxLayout()
        rmbtnlayout.setContentsMargins(0, 0, 0, 0)
        rmbtnlayout.setSpacing(0)
        rmbtnlayout.setAlignment(Qt.AlignCenter)

        rmbtnwid.setLayout(rmbtnlayout)

        rmbtn = QPushButton("REMOVE")
        rmbtn.clicked.connect(self.removeListitem)
        rmbtn.setCursor(QCursor(Qt.PointingHandCursor))
        rmbtn.setFixedSize(150, 45)
        rmbtn.setStyleSheet(
            "background-color: #8e8eb3;"
            "color: #dcdcf6;"
            "font-family: Agency FB;"
            "font-size: 18px;"
            "font-weight: bold;"
            "border-radius: 10px;"
        )

        rmbtnlayout.addWidget(rmbtn)

        contentlayout.addWidget(rmbtnwid)

    def addListitems(self, items = []):
        for item in items:
            listitem = QListWidgetItem(QIcon(item[0]), item[1])
            listitem.setToolTip(item[1])
            listitem.setSizeHint(QSize(0, 50))
            num = self.listwid.count()
            self.listwid.addItem(listitem)
            if num % 2 != 0:
                self.listwid.item(num).setBackground(QColor('#484867'))

    def addListitem(self, item = []):
        listitem = QListWidgetItem(QIcon(item[0]), item[1])
        listitem.setToolTip(item[1])
        self.listwid.addItem(listitem)

    def removeListitem(self):
        selecteditem = self.listwid.currentItem()
        if selecteditem:
            row = self.listwid.row(selecteditem)
            self.listwid.takeItem(row)