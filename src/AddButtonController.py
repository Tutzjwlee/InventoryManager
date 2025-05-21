from PySide6.QtWidgets import QPushButton, QTableWidget, QTableWidgetItem

class AddButtonController:
    def __init__(self, tableWidget: QTableWidget, addButton: QPushButton):
        self.tableWidget = tableWidget
        self.addButton = addButton
        self.addButton.clicked.connect(self.handle_addButton_click)
        self.count = 0  # cria a variável de instância

    def handle_addButton_click(self):
        self.count += 1
        print(f"Botão add Product foi clicado {self.count} vezes.")

        # Adiciona uma nova linha ao final
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

        # Preenche cada coluna da nova linha com uma célula vazia
        for col in range(self.tableWidget.columnCount()):
            self.tableWidget.setItem(rowPosition, col, QTableWidgetItem(""))
