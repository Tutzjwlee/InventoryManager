from PySide6.QtWidgets import (
    QPushButton, QTableWidget, QTableWidgetItem,
    QInputDialog, QWidget
)

class AddButtonController:
    def __init__(self, tableWidget: QTableWidget, addButton: QPushButton, parent: QWidget = None):
        self.tableWidget = tableWidget
        self.addButton = addButton
       
        self.parent = parent  # To show dialogs correctly
        self.addButton.clicked.connect(self.handle_addButton_click)
        self.count = 0

    def handle_addButton_click(self):
        self.count += 1
        print(f"Botão add Product foi clicado {self.count} vezes.")
        
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.addButton.setEnabled(False)  # Disable the button after adding a row
        # Loop through each column and ask the user to enter a value
        for col in range(self.tableWidget.columnCount()):
            headerItem = self.tableWidget.horizontalHeaderItem(col)
            columnName = headerItem.text() if headerItem else f"Column {col+1}"
            if columnName == "Full Pv" or columnName == "Full Price" or columnName == "Quantity Changed":
                
                continue
            

            text, ok = QInputDialog.getText(self.parent, "Enter Data", f"{columnName}:")
            if ok:
                self.tableWidget.setItem(rowPosition, col, QTableWidgetItem(text))
            else:
                self.tableWidget.setItem(rowPosition, col, QTableWidgetItem(""))  # empty if cancelled
        self.addButton.setEnabled(True)  # Re-enable the button after adding a row