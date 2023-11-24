from PySide6.QtWidgets import QApplication, QWidget
from rockwidget import Rockwidget
import sys
app = QApplication(sys.argv)

window = Rockwidget()
window.show()

app.exec()