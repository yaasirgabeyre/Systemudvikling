# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sekretar v2gKeBod.ui'
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
        MainWindow.resize(1045, 595)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.kalenderSekretar = QCalendarWidget(self.centralwidget)
        self.kalenderSekretar.setObjectName(u"kalenderSekretar")
        self.kalenderSekretar.setGeometry(QRect(0, 60, 541, 281))
        self.datovalg_2 = QLabel(self.centralwidget)
        self.datovalg_2.setObjectName(u"datovalg_2")
        self.datovalg_2.setGeometry(QRect(30, 0, 701, 51))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.datovalg_2.setFont(font)
        self.lokaleDropdown = QComboBox(self.centralwidget)
        self.lokaleDropdown.addItem("")
        self.lokaleDropdown.addItem("")
        self.lokaleDropdown.addItem("")
        self.lokaleDropdown.addItem("")
        self.lokaleDropdown.addItem("")
        self.lokaleDropdown.setObjectName(u"lokaleDropdown")
        self.lokaleDropdown.setGeometry(QRect(570, 370, 451, 27))
        font1 = QFont()
        font1.setPointSize(12)
        self.lokaleDropdown.setFont(font1)
        self.lokaleDropdown.setAutoFillBackground(False)
        self.lokaleDropdown.setStyleSheet(u"")
        self.tidstart = QTimeEdit(self.centralwidget)
        self.tidstart.setObjectName(u"tidstart")
        self.tidstart.setGeometry(QRect(570, 400, 451, 26))
        self.tidstart.setFont(font1)
        self.bookLokale = QPushButton(self.centralwidget)
        self.bookLokale.setObjectName(u"bookLokale")
        self.bookLokale.setGeometry(QRect(570, 490, 451, 31))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.bookLokale.setFont(font2)
        self.bookLokale.setMouseTracking(True)
        self.bookLokale.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(250, 250, 250);\n"
"}")
        self.kursusDropdown = QComboBox(self.centralwidget)
        self.kursusDropdown.addItem("")
        self.kursusDropdown.addItem("")
        self.kursusDropdown.addItem("")
        self.kursusDropdown.addItem("")
        self.kursusDropdown.addItem("")
        self.kursusDropdown.setObjectName(u"kursusDropdown")
        self.kursusDropdown.setGeometry(QRect(570, 460, 451, 27))
        self.kursusDropdown.setFont(font1)
        self.kursusDropdown.setAutoFillBackground(False)
        self.kursusDropdown.setStyleSheet(u"")
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
        self.listRequest = QListWidget(self.centralwidget)
        QListWidgetItem(self.listRequest)
        QListWidgetItem(self.listRequest)
        QListWidgetItem(self.listRequest)
        self.listRequest.setObjectName(u"listRequest")
        self.listRequest.setGeometry(QRect(570, 101, 451, 201))
        font4 = QFont()
        font4.setPointSize(11)
        self.listRequest.setFont(font4)
        self.datoValgS_2 = QLabel(self.centralwidget)
        self.datoValgS_2.setObjectName(u"datoValgS_2")
        self.datoValgS_2.setGeometry(QRect(570, 44, 451, 51))
        self.datoValgS_2.setFont(font3)
        self.godkendBooking = QPushButton(self.centralwidget)
        self.godkendBooking.setObjectName(u"godkendBooking")
        self.godkendBooking.setGeometry(QRect(810, 310, 211, 31))
        self.godkendBooking.setFont(font2)
        self.godkendBooking.setMouseTracking(True)
        self.godkendBooking.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(250, 250, 250);\n"
"}")
        self.afvisBooking = QPushButton(self.centralwidget)
        self.afvisBooking.setObjectName(u"afvisBooking")
        self.afvisBooking.setGeometry(QRect(570, 310, 211, 31))
        self.afvisBooking.setFont(font2)
        self.afvisBooking.setMouseTracking(True)
        self.afvisBooking.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(250, 250, 250);\n"
"}")
        self.tidslut = QTimeEdit(self.centralwidget)
        self.tidslut.setObjectName(u"tidslut")
        self.tidslut.setGeometry(QRect(570, 430, 451, 26))
        self.tidslut.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1045, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.datovalg_2.setText(QCoreApplication.translate("MainWindow", u"Login for administration", None))
        self.lokaleDropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"Und.lokale - A102, HC\u00d8", None))
        self.lokaleDropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"Und.lokale - A105, HC\u00d8", None))
        self.lokaleDropdown.setItemText(2, QCoreApplication.translate("MainWindow", u"Aud. - Lille UP1, DIKU", None))
        self.lokaleDropdown.setItemText(3, QCoreApplication.translate("MainWindow", u"Aud. - Niels K. Jerne, Panum", None))
        self.lokaleDropdown.setItemText(4, QCoreApplication.translate("MainWindow", u"Und.lokale - 13.1.83, Panum", None))

        self.lokaleDropdown.setCurrentText("")
        self.lokaleDropdown.setPlaceholderText(QCoreApplication.translate("MainWindow", u"V\u00e6lg lokale", None))
        self.tidstart.setSpecialValueText(QCoreApplication.translate("MainWindow", u"V\u00e6lg start tidspunkt", None))
        self.bookLokale.setText(QCoreApplication.translate("MainWindow", u"Book", None))
        self.kursusDropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"Systemudvikling - Theo exercise", None))
        self.kursusDropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"Systemudvikling - Lecture", None))
        self.kursusDropdown.setItemText(2, QCoreApplication.translate("MainWindow", u"Sygedomsl\u00e6re - Forel\u00e6sning", None))
        self.kursusDropdown.setItemText(3, QCoreApplication.translate("MainWindow", u"Sygedomsl\u00e6re - SAU", None))
        self.kursusDropdown.setItemText(4, QCoreApplication.translate("MainWindow", u"Sygedomsl\u00e6re - Caf\u00e9", None))

        self.kursusDropdown.setCurrentText("")
        self.kursusDropdown.setPlaceholderText(QCoreApplication.translate("MainWindow", u"V\u00e6lg kursus", None))
        self.datoValgS.setText(QCoreApplication.translate("MainWindow", u"{lokale}: Planlagte bookinger d. 21. marts 2022", None))
        self.datoIndholdS.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>09 - 12: Systemudvikling - Theo exercise - Und.lokale - A105, HC\u00d8</p><p>15 - 17: Systemudvikling - Lecture - Und.lokale - A105, HC\u00d8</p></body></html>", None))

        __sortingEnabled = self.listRequest.isSortingEnabled()
        self.listRequest.setSortingEnabled(False)
        ___qlistwidgetitem = self.listRequest.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"09 - 12: Systemudvikling - Theo exercise - Und.lokale - A105, HC\u00d8", None));
        ___qlistwidgetitem1 = self.listRequest.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"15 - 17: Systemudvikling - Lecture - Aud. - Lille UP1, DIKU", None));
        ___qlistwidgetitem2 = self.listRequest.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"09 - 12: Sygdomsl\u00e6re - Forel\u00e6sning - Niels K. Jerne, Panum", None));
        self.listRequest.setSortingEnabled(__sortingEnabled)

        self.datoValgS_2.setText(QCoreApplication.translate("MainWindow", u"Liste over foresp\u00f8rgsler fra undervisere", None))
        self.godkendBooking.setText(QCoreApplication.translate("MainWindow", u"Godkend", None))
        self.afvisBooking.setText(QCoreApplication.translate("MainWindow", u"Afvis", None))
        self.tidslut.setSpecialValueText(QCoreApplication.translate("MainWindow", u"V\u00e6lg slut tidspunkt", None))
    # retranslateUi

