import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QCheckBox, QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor


class CheckBox(QWidget):
    def __init__(self, w= 25, h = 25, border= '#8e8eb3', back = 'none', aback = '#8e8eb3', icon= 'images/check-solid-dark.svg'):
        super().__init__()
        self.setFixedSize(50, 50)
        self.setStyleSheet("border-radius:0;background-color:transparent;")
        self.setContentsMargins(0, 0, 0, 0)

        
        checklayout = QHBoxLayout()
        checklayout.setAlignment(Qt.AlignCenter)
        checklayout.setSpacing(0)
        checklayout.setContentsMargins(0, 0, 0, 0)

        self.check = QCheckBox()
        self.check.setContentsMargins(5, 0, 0, 0)
        self.check.setStyleSheet("""
            QCheckBox::indicator {
                width: """+str(w)+"""px;
                height: """+str(h)+"""px;
                background-color:"""+str(back)+""";
                border-radius: 5px;
                border: 1px solid """+str(border)+""";
            }
            QCheckBox::indicator:checked {
                color: black;
                background-color: """+str(aback)+""";
                image: url("""+str(icon)+""")
            }
        """)

        checklayout.addWidget(self.check)

        self.setLayout(checklayout)

class TextedCheckbox(QWidget):
    def __init__(self, text = "",w = 25, h = 25, border = '#8e8eb3', back = 'none', aback = '#8e8eb3', icon=  'images/check-solid-dark.svg'):
        super().__init__()
        
        self.setStyleSheet("border-radius:0;background-color:transparent;")
        self.setContentsMargins(0, 0, 0, 0)

        
        checklayout = QHBoxLayout()
        checklayout.setAlignment(Qt.AlignLeft)
        checklayout.setSpacing(0)
        checklayout.setContentsMargins(0, 0, 0, 0)

        checkcontent = QWidget()
        checklayout.addWidget(checkcontent)

        checkcontentlayout = QHBoxLayout()
        checkcontentlayout.setAlignment(Qt.AlignLeft)
        checkcontentlayout.setContentsMargins(0, 0, 0, 0)
        checkcontentlayout.setSpacing(0)

        self.check = QCheckBox()
        self.check.setCursor(QCursor(Qt.PointingHandCursor))
        self.check.setContentsMargins(0, 0, 0, 0)
        self.check.setStyleSheet("""
            QCheckBox::indicator {
                width: """+str(w)+"""px;
                height: """+str(h)+"""px;
                background-color:"""+str(back)+""";
                border-radius: 5px;
                border: 1px solid """+str(border)+""";
            }
            QCheckBox::indicator:checked {
                color: black;
                background-color: """+str(aback)+""";
                image: url("""+str(icon)+""")
            }
        """)

        self.text = QLabel(text)
        self.text.setStyleSheet(
            "color: #dcdcf6;"
            "font-size: 16px;"
            "font-family: Arial;"
        )

        checkcontentlayout.addWidget(self.check)
        checkcontentlayout.addWidget(self.text)

        checkcontent.setLayout(checkcontentlayout)

        self.setLayout(checklayout)
