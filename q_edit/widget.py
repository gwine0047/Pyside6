from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout,QTextEdit

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Edit Demo")

        self.text_edit = QTextEdit()
        # self.text_edit.textChanged.connect(self.text_changed)

        # buttons
        current_text = QPushButton("Print text")
        current_text.clicked.connect(self.current_text)

        # instead of creating a custom function for copy, cut, paste, undo and redo, we use the QTextEdit slot
        copy = QPushButton("Copy")
        copy.clicked.connect(self.text_edit.copy)

        cut = QPushButton("Cut")
        cut.clicked.connect(self.text_edit.cut)

        paste = QPushButton("Paste")
        paste.clicked.connect(self.text_edit.paste)

        undo = QPushButton("Undo")
        undo.clicked.connect(self.text_edit.undo)

        redo = QPushButton("Redo")
        redo.clicked.connect(self.text_edit.redo)

        set_plain_text = QPushButton("Set plain text")
        # set_plain_text.clicked.connect(self.set_plain_text)

        set_html = QPushButton("Set html")
        # set_html.clicked.connect(self.set_html)

        clear = QPushButton("clear")
        # clear.clicked.connect(self.clear)

        h_layout = QHBoxLayout()
        h_layout.addWidget(current_text)
        h_layout.addWidget(copy)
        h_layout.addWidget(cut)
        h_layout.addWidget(paste)
        h_layout.addWidget(undo)
        h_layout.addWidget(redo)
        h_layout.addWidget(set_plain_text)
        h_layout.addWidget(set_html)
        h_layout.addWidget(clear)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_edit)

        self.setLayout(v_layout)

    def current_text(self):
        print(self.text_edit.toPlainText())