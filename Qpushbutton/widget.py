from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom MainWindow")

        button = QPushButton("click")
        button.clicked.connect(self.button_clicked)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)

        layout = QVBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)

    def button_clicked(self):
        print("you just clicked the button ")
    def button_released(self):
        print("you just released the button ")
    def button_pressed(self):
        print("you just pressed the button")
    
