import sys
from PySide6.QtWidgets import QApplication
from button_holder import ButterHolder

app = QApplication(sys.argv)

window = ButterHolder()
window.show()
app.exec()