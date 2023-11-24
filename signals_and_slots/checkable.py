from PySide6.QtWidgets import QApplication, QPushButton

# this is the slot
def button_clicked(data):
    print("You clicked me, didn't you?", data)

app = QApplication()
button = QPushButton("Press me")

# Makes the button checkable. By default, it is unchecked. Furthe clicks toggled between check and uncheck
button.setCheckable(True)

# slot is written to the signal using the syntax below
button.clicked.connect(button_clicked)

button.show()
app.exec()