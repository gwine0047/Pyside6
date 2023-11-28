from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox")

        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_clicked_hard)

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question = QPushButton("question")
        button_question.clicked.connect(self.button_clicked_question)

        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)

        layout = QHBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        layout.addWidget(button_question)

        self.setLayout(layout)

# the hard way
    def button_clicked_hard(self):
        message = QMessageBox()
        message.setMinimumSize(700, 200)
        message.setWindowTitle("Message Title")
        message.setText("Something happened")
        message.setInformativeText("Do you want to do something about it?")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)

        # show the message box
        ret_val = message.exec()
        if ret_val == QMessageBox.Ok:
            print("User chose Ok")
        else:
            print("User chose Cancel")
    # an alternative
    def button_clicked_critical(self):
        ret_val = QMessageBox.critical(self, "Message Title", "Critical Message!", QMessageBox.Ok | QMessageBox.Cancel)

        if ret_val == QMessageBox.Ok:
            print("User chose ok")
        else:
            print("User chose Cancel")

    def button_clicked_question(self):
        ret_val = QMessageBox.question(self, "Message Title", "Asking a question", QMessageBox.Ok | QMessageBox.Cancel)

        if ret_val == QMessageBox.Ok:
            print("User chose ok")
        else:
            print("User chose Cancel")

    def button_clicked_information(self):
        ret_val = QMessageBox.information(self, "Message Title", "information Message!", QMessageBox.Ok | QMessageBox.Cancel)

        if ret_val == QMessageBox.Ok:
            print("User chose ok")
        else:
            print("User chose Cancel")

    def button_clicked_warning(self):
        ret_val = QMessageBox.warning(self, "Message Title", "warning Message!", QMessageBox.Ok | QMessageBox.Cancel)

        if ret_val == QMessageBox.Ok:
            print("User chose ok")
        else:
            print("User chose warning")

    def button_clicked_about(self):
        ret_val = QMessageBox.about(self, "Message Title", "about Message")

        if ret_val == QMessageBox.Ok:
            print("User chose ok")
        else:
            print("User chose Cancel")