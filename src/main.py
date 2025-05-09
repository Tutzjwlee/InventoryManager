# main.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MainWindow 
from SavingWindow import Ui_SaveWindow


class ProductManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Product Manager")

class SavingWindowApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SaveWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Saving Product Window")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductManagerApp()
    window.show()
    sys.exit(app.exec())

#self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)