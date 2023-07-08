from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QSizePolicy, QHeaderView, QLabel, QProgressBar, QPushButton
from PyQt5.QtGui import QColor, QPixmap, QIcon, QCursor
from PyQt5.QtCore import Qt, QSize
import sys
from checkbox import CheckBox


class Table(QWidget):
    def __init__(self, rows, columns, width = 950, height = 300, heads = [], types=[], sizes = [], data = []):
        super().__init__()

        self.setStyleSheet("background-color: #232339;")

        tablewidgetlayout = QVBoxLayout()
        tablewidgetlayout.setSpacing(0)
        tablewidgetlayout.setContentsMargins(0,0,0,0)
        tablewidgetlayout.setAlignment(Qt.AlignTop)

        width = width
        height = height

        # Create header widget
        header_widget = QWidget()

        header_widget.setFixedSize(width, 50)
        header_widget.setStyleSheet(
            "background-color: #8e8eb3;"
            "color: #dcdcf6;"
            "border-top-left-radius: 10px;"
            "border-top-right-radius: 10px;"
        )

        # Create horizontal layout for header widget
        header_layout = QHBoxLayout(header_widget)
        header_layout.setContentsMargins(0,0,0,0)
        header_layout.setSpacing(0)
        si = 0
        for s in sizes:
            si = si + s
        

        # Add header labels to header layout
        header_labels = heads
        i = 0
        for label in header_labels:
            if label != 'checkbox-1':
                header_label = QLabel(label)
                if len(heads) == i + 1:
                    header_label.setFixedWidth(width-si+sizes[-1]-15)
                else:
                    header_label.setFixedWidth(sizes[i])  
                
                header_label.setStyleSheet(
                    "font-size: 18px;"
                    "font-family: 'Agency FB';"
                    "font-weight: bold;"
                )
                
                header_label.setAlignment(Qt.AlignCenter)
                header_layout.addWidget(header_label)
                header_layout.setAlignment(Qt.AlignLeft)
            else:
                self.headercheck = CheckBox(border="#232339", aback='#232339', icon='images/check-solid.svg')
                self.headercheck.check.clicked.connect(self.checkall)
                self.headercheck.setCursor(QCursor(Qt.PointingHandCursor))
                self.headercheck.setContentsMargins(5, 0, 0, 0)
                header_layout.addWidget(self.headercheck)
                header_layout.setAlignment(Qt.AlignCenter)

            i = i + 1

        # Create table widget and set rows and columns
        self.tableWidget = QTableWidget()
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(columns)

        tablewidgetlayout.addWidget(header_widget)
        tablewidgetlayout.addWidget(self.tableWidget)

        

        # Hide the horizontal header
        self.tableWidget.horizontalHeader().setVisible(False)

        # Remove vertical header
        self.tableWidget.verticalHeader().setVisible(False)

        # Set header height
        header = self.tableWidget.horizontalHeader()
        header.setDefaultSectionSize(50)

        self.tableWidget.horizontalHeader().setMinimumHeight(50)
        

        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section {"
            "background-color: #8e8eb3;"
            "color: #dcdcf6;"
            "border-bottom: 1px solid #8e8eb3;"
            "border-left: none;"
            "border-right: none;"
            "}"
        )
        

        self.tableWidget.setStyleSheet(
            
            "QTableWidget {"
            "border: 1px solid #8e8eb3;"
            "color: #d6d6f0;"
            "border-bottom-left-radius: 10px;"
            "border-bottom-right-radius: 10px;"
            "padding: 0 0 10px 0;"
            "font-size: 16px;"
            "font-family: Arial;"
            "background-color: #232339;"
            "alternate-background-color: #484867;"
            "}"
            "QScrollBar:vertical {"
            "    border: 1px #8e8eb3 solid;"
            "    background-color: #232339;"
            "    width: 15px;"
            "    margin: 0px 0px 0px 0px;"
            "}"
            "QScrollBar::handle:vertical {"
            "    background-color: #8e8eb3;"
            "    min-height: 50px;"
            "}"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {"
            "    height: 0px;"
            "}"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {"
            "    background: none;"
            "}"
            "QTableView::item { border:none;border-right: 1px solid #8e8eb3;}"
            "QTableView::item:last { border-right: none; }"
            
            
        )
        
        
        self.tableWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)



        n = 0
        si = 0
        for s in sizes:
            self.tableWidget.setColumnWidth(n, s)
            si = si + s
            n = n + 1
        

        header.setStretchLastSection(True)


        self.data = data

        


        row = 0
        for i in self.data:
            
            col = 0
            for r in i:
                if types[col] == 0:
                    cell_widget = QWidget()
                    cell_widget.setStyleSheet("background: transparent;")
                    cell_layout = QHBoxLayout()


                    i = QLabel()
                    i.setFixedSize(30,30)
                    if r == 0:
                        cimg = QPixmap("images\\status\\downloading.svg")
                        i.setPixmap(cimg.scaled(30,30))
                    elif r == 1:
                        cimg = QPixmap("images\\status\\completed.svg")
                        i.setPixmap(cimg.scaled(30,30))
                    elif r == 2:
                        cimg = QPixmap("images\\status\\installing.svg")
                        i.setPixmap(cimg.scaled(30,30))
                    elif r == 3:
                        cimg = QPixmap("images\\status\\waiting.svg")
                        i.setPixmap(cimg.scaled(30,30))

                    cell_layout.addWidget(i)

                    cell_widget.setLayout(cell_layout)

                    self.tableWidget.setCellWidget(row, col, cell_widget)
                elif types[col] == 1:
                    cell_widget = QWidget()
                    cell_widget.setStyleSheet("background: transparent;")
                    cell_layout = QHBoxLayout()
                    cell_layout.setSpacing(15)

                    i = QLabel()
                    i.setFixedSize(30,30)
                    cimg = QPixmap(r[0])
                    i.setPixmap(cimg.scaled(30,30))

                    n = QLabel(r[1])
                    n.setStyleSheet(
                        "font-size: 16px;"
                        "font-family: Arial;"
                        "color: #d6d6f0;"
                    )

                    cell_layout.addWidget(i)
                    cell_layout.addWidget(n)

                    cell_widget.setLayout(cell_layout)

                    self.tableWidget.setCellWidget(row, col, cell_widget)
                elif types[col] == 3:
                    progress_bar = QProgressBar(self.tableWidget)
                    progress_bar.setMaximum(100)
                    progress_bar.setValue(50)
                    progress_bar.setTextVisible(False)
                    progress_bar.setStyleSheet(
                        "QProgressBar {"
                        "background-color: #484867;"
                        "border: 1px solid #7d7d9a;"
                        "border-radius: 5px;"
                        "}"
                        "QProgressBar::chunk {"
                        "background-color: #64ca57;"
                        "border-radius: 5px;"
                        "}"
                    )
                    progress_bar.setFixedHeight(15)
                    progress_bar.setMinimumWidth(width-si+sizes[-1]-40)
                    cell_widget = QWidget()
                    cell_widget.setStyleSheet("background: transparent;")
                    cell_layout = QVBoxLayout(cell_widget)
                    cell_layout.setContentsMargins(10,10,10,10)
                    cell_layout.addWidget(progress_bar, alignment=Qt.AlignCenter)
                    self.tableWidget.setCellWidget(row, col, cell_widget)

                elif types[col] == 2:
                    item= QTableWidgetItem(r)
                    self.tableWidget.setItem(row, col, item)
                    item.setTextAlignment(Qt.AlignCenter)


                    # Make items uneditable and unselectable
                    item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                    item.setFlags(item.flags() & ~Qt.ItemIsSelectable)

                elif types[col] == 4:
                    self.checkstate = 0
                    self.rowcheck = CheckBox()
                    self.rowcheck.check.stateChanged.connect(self.checkthestate)
                    self.rowcheck.setCursor(QCursor(Qt.PointingHandCursor))
                    self.rowcheck.setContentsMargins(5, 0, 0, 0)
                    self.tableWidget.setCellWidget(row, col, self.rowcheck)
                if types[col] == 5:
                    cell_widget = QWidget()
                    cell_widget.setStyleSheet("background: transparent;")
                    cell_layout = QHBoxLayout()


                    i = QPushButton()
                    i.setCursor(QCursor(Qt.PointingHandCursor))
                    i.setFixedSize(30,30)
                    i.setIconSize(QSize(26, 30))

                    cimg = QIcon("images\\trash-solid.svg")
                    i.setIcon(cimg)

                    cell_layout.addWidget(i)

                    cell_widget.setLayout(cell_layout)

                    self.tableWidget.setCellWidget(row, col, cell_widget)

                col = col + 1
            row = row + 1

        
        
        
        

        # Set size policy
        

        # # Set resize mode of header sections
        # header.setSectionResizeMode(QHeaderView.ResizeToContents)


        # Make headers unclickable
        header.setSectionsClickable(False)

        # Set fixed size of table widget
        self.tableWidget.setFixedSize(width, height - 50)
        self.tableWidget.item(0,4)
        # self.tableWidget.resizeColumnsToContents()
        
        
        



        self.setLayout(tablewidgetlayout)

    def checkall(self):
        
        for row in range(len(self.data)):
            check_item = self.tableWidget.cellWidget(row, 0)
            if self.headercheck.check.isChecked():
                check_item.check.setChecked(True)
            else:
                check_item.check.setChecked(False)
    def uncheck(self):
        self.headercheck.check.setChecked(False)

    def checkthestate(self):
        numofzeros = 0
        numofones = 0
        if self.tableWidget.cellWidget(len(self.data)-1, 0).check:
            for row in range(len(self.data)):
                check_item = self.tableWidget.cellWidget(row, 0)
                if check_item.check.isChecked():
                    numofones += 1
                else:
                    numofzeros += 1
            if numofones == len(self.data):
                self.checkstate = 1
            elif numofzeros == len(self.data):
                self.checkstate = 0
            elif numofones > 0 and numofones < len(self.data):
                if self.checkstate == 1:
                    self.checkstate = 2
                    self.uncheck()

    def getSelected(self):
        selected = []
        for row in range(len(self.data)):
                check_item = self.tableWidget.cellWidget(row, 0)
                if check_item.check.isChecked():
                    selected.append(row)
        return selected