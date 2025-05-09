# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SavingProductWindow.ui'
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
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_SaveWindow(object):
    def setupUi(self, SaveWindow):
        if not SaveWindow.objectName():
            SaveWindow.setObjectName(u"SaveWindow")
        SaveWindow.resize(800, 600)
        self.centralwidget = QWidget(SaveWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.salveButton = QPushButton(self.centralwidget)
        self.salveButton.setObjectName(u"salveButton")

        self.gridLayout.addWidget(self.salveButton, 1, 2, 1, 1)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")

        self.gridLayout.addWidget(self.backButton, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
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
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 3)

        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")

        self.gridLayout.addWidget(self.addButton, 1, 1, 1, 1)

        SaveWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SaveWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.menuSaving_Window = QMenu(self.menubar)
        self.menuSaving_Window.setObjectName(u"menuSaving_Window")
        SaveWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SaveWindow)
        self.statusbar.setObjectName(u"statusbar")
        SaveWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSaving_Window.menuAction())

        self.retranslateUi(SaveWindow)

        QMetaObject.connectSlotsByName(SaveWindow)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    # setupUi

    def retranslateUi(self, SaveWindow):
        SaveWindow.setWindowTitle(QCoreApplication.translate("SaveWindow", u"MainWindow", None))
        self.salveButton.setText(QCoreApplication.translate("SaveWindow", u"Salve", None))
        self.backButton.setText(QCoreApplication.translate("SaveWindow", u"Back", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SaveWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SaveWindow", u"Quantity", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SaveWindow", u"unit price", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SaveWindow", u"Unit pv", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SaveWindow", u"Date of adding", None));
        self.addButton.setText(QCoreApplication.translate("SaveWindow", u"Add", None))
        self.menuSaving_Window.setTitle(QCoreApplication.translate("SaveWindow", u"Saving Window", None))
    # retranslateUi

