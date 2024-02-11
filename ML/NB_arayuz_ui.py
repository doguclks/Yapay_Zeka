# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NB_arayuz.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1284, 891)
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
        self.BtnEgit = QPushButton(Form)
        self.BtnEgit.setObjectName(u"BtnEgit")
        self.BtnEgit.setGeometry(QRect(610, 100, 93, 28))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 140, 361, 361))
        self.LblPrecision = QLabel(Form)
        self.LblPrecision.setObjectName(u"LblPrecision")
        self.LblPrecision.setGeometry(QRect(30, 600, 171, 31))
        font = QFont()
        font.setFamilies([u"Nirmala UI"])
        font.setPointSize(10)
        self.LblPrecision.setFont(font)
        self.LblF1Score = QLabel(Form)
        self.LblF1Score.setObjectName(u"LblF1Score")
        self.LblF1Score.setGeometry(QRect(30, 680, 171, 31))
        self.LblF1Score.setFont(font)
        self.LblRecall = QLabel(Form)
        self.LblRecall.setObjectName(u"LblRecall")
        self.LblRecall.setGeometry(QRect(30, 640, 171, 31))
        self.LblRecall.setFont(font)
        self.LblSpecificity = QLabel(Form)
        self.LblSpecificity.setObjectName(u"LblSpecificity")
        self.LblSpecificity.setGeometry(QRect(30, 720, 171, 31))
        self.LblSpecificity.setFont(font)
        self.LblCDegeri_2 = QLabel(Form)
        self.LblCDegeri_2.setObjectName(u"LblCDegeri_2")
        self.LblCDegeri_2.setGeometry(QRect(530, 60, 71, 21))
        font1 = QFont()
        font1.setPointSize(9)
        self.LblCDegeri_2.setFont(font1)
        self.TxtTestSize = QLineEdit(Form)
        self.TxtTestSize.setObjectName(u"TxtTestSize")
        self.TxtTestSize.setGeometry(QRect(610, 60, 113, 22))
        self.LblAccuracy = QLabel(Form)
        self.LblAccuracy.setObjectName(u"LblAccuracy")
        self.LblAccuracy.setGeometry(QRect(30, 570, 171, 31))
        self.LblAccuracy.setFont(font)
        self.LblKomsulukDegeri_2 = QLabel(Form)
        self.LblKomsulukDegeri_2.setObjectName(u"LblKomsulukDegeri_2")
        self.LblKomsulukDegeri_2.setGeometry(QRect(430, 170, 121, 21))
        self.LblKomsulukDegeri_2.setFont(font1)
        self.TableX_train = QTableWidget(Form)
        self.TableX_train.setObjectName(u"TableX_train")
        self.TableX_train.setGeometry(QRect(430, 490, 401, 291))
        self.LblKomsulukDegeri_4 = QLabel(Form)
        self.LblKomsulukDegeri_4.setObjectName(u"LblKomsulukDegeri_4")
        self.LblKomsulukDegeri_4.setGeometry(QRect(430, 470, 121, 21))
        self.LblKomsulukDegeri_4.setFont(font1)
        self.LblKomsulukDegeri_5 = QLabel(Form)
        self.LblKomsulukDegeri_5.setObjectName(u"LblKomsulukDegeri_5")
        self.LblKomsulukDegeri_5.setGeometry(QRect(850, 470, 121, 21))
        self.LblKomsulukDegeri_5.setFont(font1)
        self.TableY_train = QTableWidget(Form)
        self.TableY_train.setObjectName(u"TableY_train")
        self.TableY_train.setGeometry(QRect(850, 490, 401, 291))
        self.TableY_test = QTableWidget(Form)
        self.TableY_test.setObjectName(u"TableY_test")
        self.TableY_test.setGeometry(QRect(850, 190, 401, 271))
        self.TableX_test = QTableWidget(Form)
        self.TableX_test.setObjectName(u"TableX_test")
        self.TableX_test.setGeometry(QRect(430, 190, 401, 271))
        self.LblKomsulukDegeri_3 = QLabel(Form)
        self.LblKomsulukDegeri_3.setObjectName(u"LblKomsulukDegeri_3")
        self.LblKomsulukDegeri_3.setGeometry(QRect(850, 170, 121, 21))
        self.LblKomsulukDegeri_3.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BtnEgit.setText(QCoreApplication.translate("Form", u"EGIT", None))
        self.label.setText("")
        self.LblPrecision.setText("")
        self.LblF1Score.setText("")
        self.LblRecall.setText("")
        self.LblSpecificity.setText("")
        self.LblCDegeri_2.setText(QCoreApplication.translate("Form", u"Test size:", None))
        self.LblAccuracy.setText("")
        self.LblKomsulukDegeri_2.setText(QCoreApplication.translate("Form", u"X-Test", None))
        self.LblKomsulukDegeri_4.setText(QCoreApplication.translate("Form", u"X-Train", None))
        self.LblKomsulukDegeri_5.setText(QCoreApplication.translate("Form", u"y-Train", None))
        self.LblKomsulukDegeri_3.setText(QCoreApplication.translate("Form", u"y-Test", None))
    # retranslateUi

