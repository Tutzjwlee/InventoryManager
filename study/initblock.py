import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Qt, QSize

class MainWindow(QMainWindow):  
    def __init__(self):
        super().__init__()
        # Set the window title
        self.setWindowTitle("Main Window")
        
        # add Widget
        # Create a button
        button = QPushButton("Click Me", self)
       
        self.setCentralWidget(button)
        self.setMinimumSize(QSize(300, 200))
        self.setMaximumSize(QSize(800, 600))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()