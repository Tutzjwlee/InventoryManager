# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProductManager.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget, QButtonGroup, QHBoxLayout)
from buttonGroupLogic import buttonGroupLogic
from AddButtonController import AddButtonController
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(945, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.addButton, 2, 0, 1, 1)

        self.editButton = QPushButton(self.centralwidget)
        self.editButton.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.editButton, 2, 2, 1, 1)

        self.removeButton = QPushButton(self.centralwidget)
        self.removeButton.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.removeButton, 2, 1, 1, 1)

        self.qtdButton = QPushButton(self.centralwidget)
        self.qtdButton.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.qtdButton, 2, 3, 1, 1)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.backButton, 2, 5, 1, 1)

        self.salveButton = QPushButton(self.centralwidget)
        self.salveButton.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.salveButton, 2, 4, 1, 1)

        
  
        

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setColumnCount(8)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 945, 30))
        self.menuProduct_Manager = QMenu(self.menubar)
        self.menuProduct_Manager.setObjectName(u"menuProduct_Manager")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuProduct_Manager.menuAction())

        # making buttons checkable
        self.addButton.setCheckable(True)
        self.editButton.setCheckable(True)
        self.removeButton.setCheckable(True)
        self.qtdButton.setCheckable(True)

        # Configura os grupos de botões
        self.mainButtons = [self.addButton, self.editButton, self.removeButton, self.qtdButton]
        self.secondaryButtons = [self.backButton, self.salveButton]
        self.groupButtons = buttonGroupLogic(self.mainButtons, self.secondaryButtons)

        self.retranslateUi(MainWindow)

        # disable save and back button on awake
        self.salveButton.setEnabled(False)
        self.backButton.setEnabled(False)

        QMetaObject.connectSlotsByName(MainWindow)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        MainWindow.setMinimumSize(QSize(1200, 600))
        
        #connecting buttons to their respective controllers
        self.addButton.clicked.connect(AddButtonController.handle_addButton_click)
        
        # Set the number of columns
        self.tableWidget.setColumnCount(8)  # or whatever number you need
        self.tableWidget.setRowCount(1)     # Only one row initially

        # Create the button
        self.insertRowButton = QPushButton("Insert Row")
        #self.insertRowButton.clicked.connect(self.insert_new_row_above)

        # Make the button stretch (fill the cell completely)
        self.insertRowButton.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )

        # Span it across all columns and add it directly
        self.tableWidget.setSpan(0, 0, 1, self.tableWidget.columnCount())
        self.tableWidget.setCellWidget(0, 0, self.insertRowButton)

        

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Add Product", None))
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"Edit Product", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"Remove Product", None))
        self.qtdButton.setText(QCoreApplication.translate("MainWindow", u"Change Quantity", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.salveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Unit Price", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Full Price", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"PV", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Full Pv", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Last Edit Quantity", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Type Edit", None));
        self.menuProduct_Manager.setTitle(QCoreApplication.translate("MainWindow", u"Product Manager", None))

    # retranslateUi
    
    
    

        