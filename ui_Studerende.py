# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StuderendeZAGzJQ.ui'
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
        MainWindow.resize(802, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(0, 70, 801, 301))
        self.datovalg_2 = QLabel(self.centralwidget)
        self.datovalg_2.setObjectName(u"datovalg_2")
        self.datovalg_2.setGeometry(QRect(40, 0, 701, 51))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.datovalg_2.setFont(font)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(40, 390, 701, 151))
        self.splitter.setOrientation(Qt.Vertical)
        self.datovalg = QLabel(self.splitter)
        self.datovalg.setObjectName(u"datovalg")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.datovalg.setFont(font1)
        self.splitter.addWidget(self.datovalg)
        self.datoindhold = QLabel(self.splitter)
        self.datoindhold.setObjectName(u"datoindhold")
        font2 = QFont()
        font2.setPointSize(12)
        self.datoindhold.setFont(font2)
        self.datoindhold.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.datoindhold.setWordWrap(True)
        self.splitter.addWidget(self.datoindhold)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 802, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.datovalg_2.setText(QCoreApplication.translate("MainWindow", u"Login som studerende", None))
        self.datovalg.setText(QCoreApplication.translate("MainWindow", u"Skema for mandag d. 21. marts 2022", None))
        self.datoindhold.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>09 - 12: Systemudvikling - Theo exercise - Und.lokale - A105, HC\u00d8</p><p>15 - 17: Systemudvikling - Lecture - Aud. - Lille UP1, DIKU</p></body></html>", None))
    # retranslateUi

