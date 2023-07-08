import typing
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QMovie

class WaitingWidget(QWidget):
    def __init__(self):
        super(WaitingWidget, self).__init__()
        self.setFixedSize(1400,680)
        self.setContentsMargins(0,0,0,0)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)

        loading = QLabel(self)
        loading.setFixedSize(200,200)

        
        movie = QMovie("images\\loading.gif")

        loading.setMovie(movie)

        movie.start()


        label = QLabel("DISCOVERING DEVICES")

        layout.addWidget(loading)
        layout.addWidget(label)

        self.setLayout(layout)

        