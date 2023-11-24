from PySide6.QtWidgets import QWidget,QPushButton,QHBoxLayout, QVBoxLayout

# QHBoxLayout: for Horizontal button layout, QVBoxLayout: for vertical button layout
# rockwidget inheriting from QWidget class
class Rockwidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rockwidget")
        button1 = QPushButton("Button1")

        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("Button2")

        button2.clicked.connect(self.button2_clicked)
        button3 = QPushButton("Button3")

# the buttonq does not know where to lay out the button, the below helps to tell where to put it
        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)

        self.setLayout(button_layout)

    def button1_clicked(self):
        print("You clicked a button1")

    def button2_clicked(self):
        print("You clicked a button2")