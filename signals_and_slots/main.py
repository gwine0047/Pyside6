from PySide6.QtWidgets import QApplication, QPushButton

#The slot: it responds whenever sth happens
def button_clicked():
    print("You clicked the button, didn't you?")

app = QApplication()
button = QPushButton("Press me")

# clicked is a signal of QPushButton. It is emitted when you click on the button
button.clicked.connect(button_clicked)
button.show()
app.exec()