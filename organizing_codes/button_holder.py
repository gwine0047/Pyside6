# Importing the components needed
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget, QPushButton, QMainWindow

class ButterHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("bUTTON Holder App")
        button = QPushButton("Press me!")
        # set up the button as our central widget.
        self.setCentralWidget(button)
