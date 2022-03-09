# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
        MainWindow.setEnabled(True)
        MainWindow.resize(523, 394)
        MainWindow.setDocumentMode(False)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mostrar_pushButton = QPushButton(self.centralwidget)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout_2.addWidget(self.mostrar_pushButton, 1, 1, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.agregar_final_pushButton = QPushButton(self.groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout.addWidget(self.agregar_final_pushButton, 6, 0, 1, 2)

        self.publicado_spinBox = QSpinBox(self.groupBox)
        self.publicado_spinBox.setObjectName(u"publicado_spinBox")
        self.publicado_spinBox.setMinimum(2000)
        self.publicado_spinBox.setMaximum(2022)

        self.gridLayout.addWidget(self.publicado_spinBox, 3, 1, 1, 1)

        self.editorial_lineEdit = QLineEdit(self.groupBox)
        self.editorial_lineEdit.setObjectName(u"editorial_lineEdit")

        self.gridLayout.addWidget(self.editorial_lineEdit, 4, 1, 1, 1)

        self.autor_lineEdit = QLineEdit(self.groupBox)
        self.autor_lineEdit.setObjectName(u"autor_lineEdit")

        self.gridLayout.addWidget(self.autor_lineEdit, 2, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.modificar_pushButton = QPushButton(self.groupBox)
        self.modificar_pushButton.setObjectName(u"modificar_pushButton")

        self.gridLayout.addWidget(self.modificar_pushButton, 9, 0, 1, 2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.eliminar_pushButton = QPushButton(self.groupBox)
        self.eliminar_pushButton.setObjectName(u"eliminar_pushButton")

        self.gridLayout.addWidget(self.eliminar_pushButton, 8, 0, 1, 2)

        self.agregar_pushButton = QPushButton(self.groupBox)
        self.agregar_pushButton.setObjectName(u"agregar_pushButton")

        self.gridLayout.addWidget(self.agregar_pushButton, 5, 0, 1, 2)

        self.titulo_lineEdit = QLineEdit(self.groupBox)
        self.titulo_lineEdit.setObjectName(u"titulo_lineEdit")

        self.gridLayout.addWidget(self.titulo_lineEdit, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)

        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setMaximum(1000)

        self.gridLayout.addWidget(self.id_spinBox, 7, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 523, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.titulo_lineEdit, self.autor_lineEdit)
        QWidget.setTabOrder(self.autor_lineEdit, self.publicado_spinBox)
        QWidget.setTabOrder(self.publicado_spinBox, self.editorial_lineEdit)
        QWidget.setTabOrder(self.editorial_lineEdit, self.agregar_pushButton)
        QWidget.setTabOrder(self.agregar_pushButton, self.plainTextEdit)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

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
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Libro", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar final", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Plubicado", None))
        self.modificar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Autor", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Editorial", None))
        self.eliminar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.agregar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

