import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDateTimeEdit, QPushButton

class DateTimePickerWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Create the QDateTimeEdit widget
        self.datetime_edit = QDateTimeEdit(self)
        self.datetime_edit.setCalendarPopup(True)  # Enable calendar popup for date selection
        

        # Set the display format to include both date and time
        self.datetime_edit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")

        # Create a button to retrieve the selected date and time
        self.button = QPushButton("Get Selected Date and Time")
        self.button.clicked.connect(self.get_selected_datetime)

        layout.addWidget(self.datetime_edit)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def get_selected_datetime(self):
        selected_datetime = self.datetime_edit.dateTime()
        print("Selected Date and Time:", selected_datetime.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DateTimePickerWidget()
    window.show()
    sys.exit(app.exec_())
