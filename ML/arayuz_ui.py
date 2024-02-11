# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arayuz.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1160, 530)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(0, 170, 127, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        Form.setPalette(palette)
        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(420, 20, 721, 301))
        self.BtnDYukle = QPushButton(Form)
        self.BtnDYukle.setObjectName(u"BtnDYukle")
        self.BtnDYukle.setGeometry(QRect(620, 380, 261, 81))
        font = QFont()
        font.setPointSize(12)
        self.BtnDYukle.setFont(font)
        self.BtnANN = QPushButton(Form)
        self.BtnANN.setObjectName(u"BtnANN")
        self.BtnANN.setGeometry(QRect(30, 330, 261, 81))
        self.BtnANN.setFont(font)
        self.BtnKNN = QPushButton(Form)
        self.BtnKNN.setObjectName(u"BtnKNN")
        self.BtnKNN.setGeometry(QRect(30, 30, 261, 81))
        font1 = QFont()
        font1.setPointSize(14)
        self.BtnKNN.setFont(font1)
        self.BtnNaive = QPushButton(Form)
        self.BtnNaive.setObjectName(u"BtnNaive")
        self.BtnNaive.setGeometry(QRect(30, 230, 261, 81))
        self.BtnNaive.setFont(font1)
        self.BtnRandomForest = QPushButton(Form)
        self.BtnRandomForest.setObjectName(u"BtnRandomForest")
        self.BtnRandomForest.setGeometry(QRect(30, 130, 261, 81))
        self.BtnRandomForest.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BtnDYukle.setText(QCoreApplication.translate("Form", u"VERISETINI GOSTER", None))
        self.BtnANN.setText(QCoreApplication.translate("Form", u"ANN", None))
        self.BtnKNN.setText(QCoreApplication.translate("Form", u"KNN", None))
        self.BtnNaive.setText(QCoreApplication.translate("Form", u"NAIVE", None))
        self.BtnRandomForest.setText(QCoreApplication.translate("Form", u"RANDOM FOREST", None))
    # retranslateUi

