from PyQt5.QtCore import Qt, QPropertyAnimation, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5 import QtGui, QtCore
class WaitingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.startAnimation()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel(self)
        layout.addWidget(self.label)

        self.setFixedSize(100, 100)
        self.setWindowTitle('Waiting Widget')
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")

    def startAnimation(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.rotate)
        self.timer.start(100)  # Interval in milliseconds
        self.angle = 0

    def rotate(self):
        self.angle += 30
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        rect = self.contentsRect()
        center = rect.center()

        # Draw the animation
        painter.translate(center)
        painter.rotate(self.angle)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.darkGray)

        size = min(rect.width(), rect.height()) * 0.5
        rect = QtCore.QRectF(-size, -size, size * 2, size * 2)
        painter.drawEllipse(rect)

if __name__ == '__main__':
    app = QApplication([])
    window = WaitingWidget()
    window.show()
    app.exec_()
