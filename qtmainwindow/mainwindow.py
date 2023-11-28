from PySide6.QtWidgets import QMainWindow,QToolBar, QPushButton, QStatusBar, QHBoxLayout
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app #declare an ap member
        self.setWindowTitle("Custom MainWindow")

        # Menubar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        # Adding a bunch of other menu options
        edit_menu = menu_bar.addMenu("Window")
        edit_menu = menu_bar.addMenu("Setting")
        edit_menu = menu_bar.addMenu("Help")

        # working with toolbars
        toolbar = QToolBar("Custom Main toolbar")
        toolbar.setIconSize(QSize (16, 16))
        self.addToolBar(toolbar)

        # add the quit action to the toolbar
        toolbar.addAction(quit_action)

        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        # adding action1 to the toolbar
        toolbar.addAction(action1)


        action2 = QAction(QIcon("Aim.png"),"Aim", self)
        action2.setStatusTip("Status message for some action")
        action2.triggered.connect(self.toolbar_button_click)
        action2.setCheckable(True)
        # adding action1 to the toolbar
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click here"))

        # status bar
        self.setStatusBar(QStatusBar(self))

        button = QPushButton("BUTTON")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
        
        # layout for button
        # layout = QHBoxLayout()
        # layout.addWidget(button)

    # defining a quit method
    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        print("action triggered")
        self.statusBar().showMessage("Message onstatus bar", 3000)

    def button_clicked(self):
        print("The addition of 2 and 3 =", 2 + 3)