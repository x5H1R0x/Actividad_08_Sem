# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1033, 600)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 0, 176, 319))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.addEnd_pushButton = QPushButton(self.groupBox)
        self.addEnd_pushButton.setObjectName(u"addEnd_pushButton")

        self.gridLayout_2.addWidget(self.addEnd_pushButton, 9, 2, 1, 1)

        self.blue_spinBox = QSpinBox(self.groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.blue_spinBox, 8, 1, 1, 2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)

        self.originY_spinBox = QSpinBox(self.groupBox)
        self.originY_spinBox.setObjectName(u"originY_spinBox")
        self.originY_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.originY_spinBox, 2, 1, 1, 2)

        self.showListParticle_pushButton = QPushButton(self.groupBox)
        self.showListParticle_pushButton.setObjectName(u"showListParticle_pushButton")

        self.gridLayout_2.addWidget(self.showListParticle_pushButton, 10, 0, 1, 3)

        self.originX_label = QLabel(self.groupBox)
        self.originX_label.setObjectName(u"originX_label")

        self.gridLayout_2.addWidget(self.originX_label, 1, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 8, 0, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.red_spinBox, 6, 1, 1, 2)

        self.destY_spinBox = QSpinBox(self.groupBox)
        self.destY_spinBox.setObjectName(u"destY_spinBox")
        self.destY_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.destY_spinBox, 4, 1, 1, 2)

        self.destX_spinBox = QSpinBox(self.groupBox)
        self.destX_spinBox.setObjectName(u"destX_spinBox")
        self.destX_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.destX_spinBox, 3, 1, 1, 2)

        self.green_spinBox = QSpinBox(self.groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.green_spinBox, 7, 1, 1, 2)

        self.originX_label_2 = QLabel(self.groupBox)
        self.originX_label_2.setObjectName(u"originX_label_2")

        self.gridLayout_2.addWidget(self.originX_label_2, 0, 0, 1, 1)

        self.originX_spinBox = QSpinBox(self.groupBox)
        self.originX_spinBox.setObjectName(u"originX_spinBox")
        self.originX_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.originX_spinBox, 1, 1, 1, 2)

        self.addToStart_pushButton = QPushButton(self.groupBox)
        self.addToStart_pushButton.setObjectName(u"addToStart_pushButton")

        self.gridLayout_2.addWidget(self.addToStart_pushButton, 9, 0, 1, 2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)

        self.originY_label = QLabel(self.groupBox)
        self.originY_label.setObjectName(u"originY_label")

        self.gridLayout_2.addWidget(self.originY_label, 2, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 7, 0, 1, 1)

        self.speed_spinBox = QSpinBox(self.groupBox)
        self.speed_spinBox.setObjectName(u"speed_spinBox")
        self.speed_spinBox.setMaximum(99999)

        self.gridLayout_2.addWidget(self.speed_spinBox, 5, 1, 1, 2)

        self.id_lineEdit = QLineEdit(self.groupBox)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout_2.addWidget(self.id_lineEdit, 0, 1, 1, 2)

        self.particle_PlainText = QPlainTextEdit(self.tab)
        self.particle_PlainText.setObjectName(u"particle_PlainText")
        self.particle_PlainText.setGeometry(QRect(280, 0, 271, 361))
        self.tabWidget.addTab(self.tab, "")
        self.Table = QWidget()
        self.Table.setObjectName(u"Table")
        self.gridLayout = QGridLayout(self.Table)
        self.gridLayout.setObjectName(u"gridLayout")
        self.particle_tableWidget = QTableWidget(self.Table)
        self.particle_tableWidget.setObjectName(u"particle_tableWidget")

        self.gridLayout.addWidget(self.particle_tableWidget, 0, 0, 1, 3)

        self.search_lineEdit = QLineEdit(self.Table)
        self.search_lineEdit.setObjectName(u"search_lineEdit")

        self.gridLayout.addWidget(self.search_lineEdit, 1, 0, 1, 1)

        self.search_pushButton = QPushButton(self.Table)
        self.search_pushButton.setObjectName(u"search_pushButton")

        self.gridLayout.addWidget(self.search_pushButton, 1, 1, 1, 1)

        self.show_pushButton = QPushButton(self.Table)
        self.show_pushButton.setObjectName(u"show_pushButton")

        self.gridLayout.addWidget(self.show_pushButton, 1, 2, 1, 1)

        self.tabWidget.addTab(self.Table, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1033, 21))
        self.menuAbrir = QMenu(self.menubar)
        self.menuAbrir.setObjectName(u"menuAbrir")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbrir.menuAction())
        self.menuAbrir.addAction(self.actionAbrir)
        self.menuAbrir.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.addEnd_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destino X:", None))
        self.showListParticle_pushButton.setText(QCoreApplication.translate("MainWindow", u"MOSTRAR", None))
        self.originX_label.setText(QCoreApplication.translate("MainWindow", u"Origen X:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Azul:", None))
        self.originX_label_2.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.addToStart_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Rojo:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destino Y:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.originY_label.setText(QCoreApplication.translate("MainWindow", u"Origen Y:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Verde:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.search_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.show_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Table), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.menuAbrir.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

