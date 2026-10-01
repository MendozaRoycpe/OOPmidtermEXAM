import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

class SpecialMidtermApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("OOP MIDTERM EXAM NUMBER 2")
        self.setGeometry(200, 200, 400, 300)

        # Create button
        self.btn = QPushButton("Click to Change Color", self) #I just copied what is there on the task, the word itself
        self.btn.move(130, 130)
        self.btn.resize(140, 35)

        # Connect click event to slot
        self.btn.clicked.connect(self.change_color)

        self.show()

    def change_color(self):
        # Change button background color to yellow
        self.btn.setStyleSheet("background-color: yellow;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpecialMidtermApp()
    sys.exit(app.exec())