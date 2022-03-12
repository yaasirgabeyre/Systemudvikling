# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UnderviseraoPxVg.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(961, 595)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.kalenderUnderviser = QCalendarWidget(self.centralwidget)
        self.kalenderUnderviser.setObjectName(u"kalenderUnderviser")
        self.kalenderUnderviser.setGeometry(QRect(0, 60, 961, 281))
        self.datovalg_2 = QLabel(self.centralwidget)
        self.datovalg_2.setObjectName(u"datovalg_2")
        self.datovalg_2.setGeometry(QRect(30, 0, 701, 51))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.datovalg_2.setFont(font)
        self.forsporgselTid = QTimeEdit(self.centralwidget)
        self.forsporgselTid.setObjectName(u"forsporgselTid")
        self.forsporgselTid.setGeometry(QRect(570, 400, 361, 26))
        font1 = QFont()
        font1.setPointSize(12)
        self.forsporgselTid.setFont(font1)
        self.lavForsporgsel_2 = QPushButton(self.centralwidget)
        self.lavForsporgsel_2.setObjectName(u"lavForsporgsel_2")
        self.lavForsporgsel_2.setGeometry(QRect(570, 470, 361, 31))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.lavForsporgsel_2.setFont(font2)
        self.lavForsporgsel_2.setMouseTracking(True)
        self.lavForsporgsel_2.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(250, 250, 250);\n"
"}")
        self.kursusDropdownForporgsel = QComboBox(self.centralwidget)
        self.kursusDropdownForporgsel.addItem("")
        self.kursusDropdownForporgsel.addItem("")
        self.kursusDropdownForporgsel.addItem("")
        self.kursusDropdownForporgsel.addItem("")
        self.kursusDropdownForporgsel.addItem("")
        self.kursusDropdownForporgsel.setObjectName(u"kursusDropdownForporgsel")
        self.kursusDropdownForporgsel.setGeometry(QRect(570, 430, 361, 27))
        self.kursusDropdownForporgsel.setFont(font1)
        self.kursusDropdownForporgsel.setAutoFillBackground(False)
        self.kursusDropdownForporgsel.setStyleSheet(u"")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(30, 360, 511, 191))
        self.splitter.setOrientation(Qt.Vertical)
        self.datoValgS = QLabel(self.splitter)
        self.datoValgS.setObjectName(u"datoValgS")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.datoValgS.setFont(font3)
        self.splitter.addWidget(self.datoValgS)
        self.datoIndholdS = QLabel(self.splitter)
        self.datoIndholdS.setObjectName(u"datoIndholdS")
        self.datoIndholdS.setFont(font1)
        self.datoIndholdS.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.datoIndholdS.setWordWrap(True)
        self.splitter.addWidget(self.datoIndholdS)
        self.lavForsporgsel = QLabel(self.centralwidget)
        self.lavForsporgsel.setObjectName(u"lavForsporgsel")
        self.lavForsporgsel.setGeometry(QRect(570, 350, 361, 55))
        self.lavForsporgsel.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 961, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.datovalg_2.setText(QCoreApplication.translate("MainWindow", u"Login som underviser", None))
        self.forsporgselTid.setSpecialValueText(QCoreApplication.translate("MainWindow", u"V\u00e6lg tidspunkt", None))
        self.lavForsporgsel_2.setText(QCoreApplication.translate("MainWindow", u"Lav foresp\u00f8rgsel", None))
        self.kursusDropdownForporgsel.setItemText(0, QCoreApplication.translate("MainWindow", u"Systemudvikling - Theo exercise", None))
        self.kursusDropdownForporgsel.setItemText(1, QCoreApplication.translate("MainWindow", u"Systemudvikling - Lecture", None))
        self.kursusDropdownForporgsel.setItemText(2, QCoreApplication.translate("MainWindow", u"Sygedomsl\u00e6re - Forel\u00e6sning", None))
        self.kursusDropdownForporgsel.setItemText(3, QCoreApplication.translate("MainWindow", u"Sygedomsl\u00e6re - SAU", None))
        self.kursusDropdownForporgsel.setItemText(4, QCoreApplication.translate("MainWindow", u"Sygedomsl\u00e6re - Caf\u00e9", None))

        self.kursusDropdownForporgsel.setCurrentText("")
        self.kursusDropdownForporgsel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"V\u00e6lg kursus", None))
        self.datoValgS.setText(QCoreApplication.translate("MainWindow", u"Planlagte bookinger d. 21. marts 2022", None))
        self.datoIndholdS.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>09 - 12: Systemudvikling - Theo exercise - Und.lokale - A105, HC\u00d8</p><p>15 - 17: Systemudvikling - Lecture - Aud. - Lille UP1, DIKU</p></body></html>", None))
        self.lavForsporgsel.setText(QCoreApplication.translate("MainWindow", u"Lav lokale foresp\u00f8rgelse", None))
    # retranslateUi

