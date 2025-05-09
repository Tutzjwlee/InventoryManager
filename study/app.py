from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton

import sys

app = QApplication(sys.argv)

window = QWidget()

window.show()

app.exec()

# all widgets without a parent are invisible by default, so we must always .show() to make it visible
# all top level widgets are windows, so you can make a window with any widget you like

# the app.exec() starts the event loop
# The core of every Qt Applications is the QApplication class. Every application needs one, and only one, QApplication Oobject to function.
# this object holds the event loop of yur application - the core loop which governs all user interaction with the GUI