from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout, QLabel, QLineEdit

# QLineEdit is used to collect data from users
# QLabel is used as a you know label, static texts
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel and QLineEdit")

        # A set of signals we can connect to
        label = QLabel("Fullname : ")
        self.line_edit = QLineEdit()

        # when text changes
        self.line_edit.textChanged.connect(self.text_changed)

        # cursor change
        # self.line_edit.cursorPositionChanged.connect(self.cursor_changed)

        # when enter key is hit
        # self.line_edit.editingFinished.connect(self.editing_finished)

        # when enter key is hit
        # self.line_edit.returnPressed.connect(self.return_pressed)

        # when user highlights and selects
        self.line_edit.selectionChanged.connect(self.selection_changed)

        # show edited text
        self.line_edit.textEdited.connect(self.text_edited)

        button = QPushButton("Grab data")
        button.clicked.connect(self.button_clicked)
        self.text_holder = QLabel("I am here")

        # layouts : horizontal and vertical
        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder)

        self.setLayout(v_layout)

    def button_clicked(self):
        # print("Your name is :",self.line_edit.text())
        self.text_holder.setText(self.line_edit.text())

    def text_changed(self):
        self.text_holder.setText(self.line_edit.text())

    def cursor_changed(self, old, new):
        print("cursor old position: ",old,"cursor new position : ", new)

    def editing_finished(self):
        print("Done editing. User hit enter")

    def return_pressed(self):
        print("return is pressed. ie User hits enter")

    def selection_changed(self):
        print("Selected text: ", self.line_edit.selectedText())

    def text_edited(self, new_text):
        print("Text edited. New text: ", new_text)