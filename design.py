import sys
import os
from PyQt5.QtCore import Qt, QPoint, QSize
from PyQt5.QtGui import QFontDatabase, QCursor, QColor, QPixmap

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QHBoxLayout, QPushButton, QStackedLayout, QTabWidget,
    QLabel, QGraphicsDropShadowEffect, QTableWidget, QFileDialog
)

from table import Table
from checkbox import TextedCheckbox
from itemlist import ItemListPlus
from getonline import GetOnline
from install.send2 import Send
from install.compress import Compress
from icoextract import IconExtractor

class Design(QWidget):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        

        designlayout = QHBoxLayout()
        designlayout.setAlignment(Qt.AlignLeft)
        designlayout.setContentsMargins(0, 0, 0, 0)
        designlayout.setSpacing(0)


        designwid = QWidget()

        designwidlayout = QHBoxLayout()
        designwidlayout.setAlignment(Qt.AlignTop)
        designwidlayout.setContentsMargins(50, 60, 0, 0)
        designwidlayout.setSpacing(60)

        designwid.setLayout(designwidlayout)


        self.table = self.check_online()

        self.tablewid = QWidget()
        self.tablewid.setFixedSize(715, 565)
        self.tablewid.setContentsMargins(0, 0, 0, 0)

        self.tablewidlayout = QHBoxLayout()
        self.tablewid.setLayout(self.tablewidlayout)
        

        self.tablewidlayout.addWidget(self.table)
        self.tablewidlayout.setContentsMargins(0, 0, 0, 0)
        self.tablewidlayout.setSpacing(0)


        options = QWidget()
        # options.setStyleSheet("background-color:black;")
        options.setFixedHeight(565)

        optionslayout = QVBoxLayout()
        optionslayout.setSpacing(40)
        optionslayout.setContentsMargins(0, 0, 0, 0)
        optionslayout.setAlignment(Qt.AlignTop)

        options.setLayout(optionslayout)

        fileslayout = QHBoxLayout()
        fileslayout.setSpacing(20)
        fileslayout.setContentsMargins(0, 0, 0, 0)
        optionslayout.addLayout(fileslayout)
        

        filebtn = QPushButton("Select Execution File")
        filebtn.setCursor(QCursor(Qt.PointingHandCursor))
        filebtn.setFixedSize(200, 50)
        filebtn.setStyleSheet(
            "background-color: #8e8eb3;"
            "color: #dcdcf6;"
            "font-size: 22px;"
            "font-weight: bold;"
            "font-family: Agency FB;"
            "border:none;"
            "border-radius: 10px;"
        )
        self.paths = []
        filebtn.clicked.connect(self.open_file_dialog)

        self.filetext = QLabel("there is no file selected")
        self.filetext.setStyleSheet(
            "color: #dcdcf6;"
            "font-size: 16px;"
            "font-family: Arial;"
        )

        fileslayout.addWidget(filebtn)
        fileslayout.addWidget(self.filetext)


        finlayout = QVBoxLayout()
        finlayout.setContentsMargins(0, 0, 0, 0)
        finlayout.setSpacing(20)

        fintitle = QLabel("When Finished:")
        fintitle.setStyleSheet(
            "color: #dcdcf6;"
            "font-size: 16px;"
            "font-family: Arial;"
            "font-weight: bold;"
        )

        finchecklayout = QHBoxLayout()
        finchecklayout.setAlignment(Qt.AlignLeft)
        finchecklayout.setContentsMargins(0, 0, 0, 0)
        finchecklayout.setSpacing(40)

        fincheck1 = TextedCheckbox(text='Restart')
        fincheck2 = TextedCheckbox(text='Shutdown')
        fincheck3 = TextedCheckbox(text='Lock')
        fincheck4 = TextedCheckbox(text='Sleep')

        finchecklayout.addWidget(fincheck1)
        finchecklayout.addWidget(fincheck2)
        finchecklayout.addWidget(fincheck3)
        finchecklayout.addWidget(fincheck4)

        finlayout.addWidget(fintitle)
        finlayout.addLayout(finchecklayout)

        optionslayout.addLayout(finlayout)

        poplayout = QVBoxLayout()
        poplayout.setContentsMargins(0, 0, 0, 0)
        poplayout.setSpacing(20)

        poptitle = QLabel("Program Options:")
        poptitle.setStyleSheet(
            "color: #dcdcf6;"
            "font-size: 16px;"
            "font-family: Arial;"
            "font-weight: bold;"
        )
        popchecklayout = QHBoxLayout()
        popchecklayout.setAlignment(Qt.AlignLeft)
        popchecklayout.setContentsMargins(0, 0, 0, 0)
        popchecklayout.setSpacing(40)

        popcheck1 = TextedCheckbox(text='Add To Desktop')
        popcheck2 = TextedCheckbox(text='Add To Taskbar')
        popcheck3 = TextedCheckbox(text='Auto Start')

        popchecklayout.addWidget(popcheck1)
        popchecklayout.addWidget(popcheck2)
        popchecklayout.addWidget(popcheck3)

        poplayout.addWidget(poptitle)
        poplayout.addLayout(popchecklayout)

        optionslayout.addLayout(poplayout)


        plistlayout = QHBoxLayout()
        plistlayout.setAlignment(Qt.AlignLeft)
        plistlayout.setContentsMargins(0, 0, 0, 0)
        plistlayout.setSpacing(0)

        plistwid = QWidget()
        # plistwid.setStyleSheet("background-color: yellow;")
        plistwid.setLayout(plistlayout)

        self.list = ItemListPlus(width=250, height=250)
        items = []
        self.list.addListitems(items=items)


        startbtn = QPushButton("START")
        startbtn.clicked.connect(self.send_file)
        startbtn.setStyleSheet(
            """
            background-color: #dcdcf6;
            border-radius: 90px;
            font-size: 35px;
            font-family: 'Viga', sans-serif;
            color: #232339;
            """
        )
        startbtn.setFixedHeight(180)
        startbtn.setFixedWidth(180)
        startbtn.setCursor(QCursor(Qt.PointingHandCursor))
        
        
        startbtnshadow = QGraphicsDropShadowEffect()
        startbtnshadow.setBlurRadius(15)
        startbtnshadow.setColor(QColor(220, 220, 246).lighter())
        startbtnshadow.setOffset(0)
    

        startbtn.setGraphicsEffect(startbtnshadow)

        sbtnlayout = QVBoxLayout()
        sbtnlayout.setSpacing(0)
        sbtnlayout.setContentsMargins(0,0,0,0)
        sbtnlayout.setAlignment(Qt.AlignCenter)

        sbtnlayout.addWidget(startbtn)

    

        plistlayout.addWidget(self.list)
        plistlayout.addLayout(sbtnlayout)


        optionslayout.addWidget(plistwid)
        


        designwidlayout.addWidget(self.tablewid)
        designwidlayout.addWidget(options)


        designlayout.addWidget(designwid)

        self.setLayout(designlayout)

    def check_online(self):
        heads = ["checkbox-1", "DEVICE NAME","DEVICE MAC", "DEVICE IP"]
        types = [4, 1, 2, 2]
        sizes = [50, 200, 200, 200]
        data = []

        online = GetOnline('192.168.2.')
        self.devices = online.devices_data

        for device in self.devices:
            data.append([1, ["images\\profile_img\\pc1.png", device[0]], device[1], device[2]])
        
        table = Table(15, 4, 715, 565, heads, types, sizes, data)
        table.setStyleSheet("")

        return table
    
    def send_file(self):



        selected = self.table.getSelected()
        for dev in selected:
            print(dev)
            device = self.devices[dev]

            name = self.filename.split('.')[0]
            
            com = Compress(name, self.path).getfile()
            Send(device[2], 12345, com)
    
    def open_file_dialog(self):

        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setDirectory("C:\\Program Files\\Audacity")
        file_dialog.selectFile("Audacity.exe")

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            folder_path = QFileDialog.directory(file_dialog).path()
            print("Selected File:", file_path)
            print("Folder Path:", folder_path)

            self.path = folder_path
            
            self.filename = os.path.basename(file_path)
            self.filetext.setText(self.filename)

            name = self.filename.split('.')[0]

            extractor = IconExtractor(file_path)
            extractor.export_icon(r'install\icons\\'+name+'.ico', 0)


            self.add_program([r'install\icons\\'+name+'.ico', self.filename])

    def add_program(self, item):
        self.list.addListitem(item=item)

