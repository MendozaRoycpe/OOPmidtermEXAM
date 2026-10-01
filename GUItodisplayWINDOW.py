import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

class MidtermApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Midterm in OOP")
        self.setGeometry(200, 200, 800, 500)

        #left label for the input field "Enter your fullname:"
        self.label = QLabel("Enter your fullname:", self)
        self.label.move(80, 80)
        self.label.setStyleSheet("color: green;")

        #input line box
        self.input_field = QLineEdit(self)
        self.input_field.move(220, 100)
        self.input_field.resize(220, 50)

        #button with the click to display your fullname and click it tp display the fullname in the output field
        self.btn = QPushButton("Click to display your Fullname", self)
        self.btn.move(50, 150)
        self.btn.setStyleSheet("color: lightblue;")
        self.btn.clicked.connect(self.display_fullname)

        #show the copied text
        self.output_field = QLineEdit(self)
        self.output_field.move(220, 150)
        self.output_field.resize(220, 50)

        self.show()

    def display_fullname(self):
        # copies the input field data into the output
        self.output_field.setText(self.input_field.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MidtermApp()
    sys.exit(app.exec())