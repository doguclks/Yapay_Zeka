# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'knn_arayuz.ui'
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
        Form.resize(1327, 772)
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
        self.TxtTestOrani = QLineEdit(Form)
        self.TxtTestOrani.setObjectName(u"TxtTestOrani")
        self.TxtTestOrani.setGeometry(QRect(470, 30, 113, 22))
        self.TxtKomsulukDegeri = QLineEdit(Form)
        self.TxtKomsulukDegeri.setObjectName(u"TxtKomsulukDegeri")
        self.TxtKomsulukDegeri.setGeometry(QRect(470, 70, 113, 22))
        self.LblTestOrani = QLabel(Form)
        self.LblTestOrani.setObjectName(u"LblTestOrani")
        self.LblTestOrani.setGeometry(QRect(370, 30, 81, 16))
        font = QFont()
        font.setPointSize(9)
        self.LblTestOrani.setFont(font)
        self.LblKomsulukDegeri = QLabel(Form)
        self.LblKomsulukDegeri.setObjectName(u"LblKomsulukDegeri")
        self.LblKomsulukDegeri.setGeometry(QRect(350, 70, 121, 21))
        self.LblKomsulukDegeri.setFont(font)
        self.TxtEgit = QPushButton(Form)
        self.TxtEgit.setObjectName(u"TxtEgit")
        self.TxtEgit.setGeometry(QRect(610, 30, 93, 61))
        self.LblAccuracy = QLabel(Form)
        self.LblAccuracy.setObjectName(u"LblAccuracy")
        self.LblAccuracy.setGeometry(QRect(60, 530, 221, 31))
        font1 = QFont()
        font1.setFamilies([u"Nirmala UI"])
        font1.setPointSize(10)
        self.LblAccuracy.setFont(font1)
        self.LblPrecision = QLabel(Form)
        self.LblPrecision.setObjectName(u"LblPrecision")
        self.LblPrecision.setGeometry(QRect(60, 570, 221, 31))
        self.LblPrecision.setFont(font1)
        self.LblRecall = QLabel(Form)
        self.LblRecall.setObjectName(u"LblRecall")
        self.LblRecall.setGeometry(QRect(60, 620, 221, 21))
        self.LblRecall.setFont(font1)
        self.LblF1Score = QLabel(Form)
        self.LblF1Score.setObjectName(u"LblF1Score")
        self.LblF1Score.setGeometry(QRect(60, 650, 221, 31))
        self.LblF1Score.setFont(font1)
        self.LblSpecificity = QLabel(Form)
        self.LblSpecificity.setObjectName(u"LblSpecificity")
        self.LblSpecificity.setGeometry(QRect(60, 690, 221, 31))
        self.LblSpecificity.setFont(font1)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 30, 61, 71))
        font2 = QFont()
        font2.setPointSize(18)
        self.label.setFont(font2)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 130, 361, 311))
        self.TableX_test = QTableWidget(Form)
        self.TableX_test.setObjectName(u"TableX_test")
        self.TableX_test.setGeometry(QRect(460, 120, 401, 271))
        self.TableX_train = QTableWidget(Form)
        self.TableX_train.setObjectName(u"TableX_train")
        self.TableX_train.setGeometry(QRect(460, 420, 401, 291))
        self.TableY_test = QTableWidget(Form)
        self.TableY_test.setObjectName(u"TableY_test")
        self.TableY_test.setGeometry(QRect(880, 120, 401, 271))
        self.TableY_train = QTableWidget(Form)
        self.TableY_train.setObjectName(u"TableY_train")
        self.TableY_train.setGeometry(QRect(880, 420, 401, 291))
        self.LblKomsulukDegeri_2 = QLabel(Form)
        self.LblKomsulukDegeri_2.setObjectName(u"LblKomsulukDegeri_2")
        self.LblKomsulukDegeri_2.setGeometry(QRect(460, 100, 121, 21))
        self.LblKomsulukDegeri_2.setFont(font)
        self.LblKomsulukDegeri_3 = QLabel(Form)
        self.LblKomsulukDegeri_3.setObjectName(u"LblKomsulukDegeri_3")
        self.LblKomsulukDegeri_3.setGeometry(QRect(880, 100, 121, 21))
        self.LblKomsulukDegeri_3.setFont(font)
        self.LblKomsulukDegeri_4 = QLabel(Form)
        self.LblKomsulukDegeri_4.setObjectName(u"LblKomsulukDegeri_4")
        self.LblKomsulukDegeri_4.setGeometry(QRect(460, 400, 121, 21))
        self.LblKomsulukDegeri_4.setFont(font)
        self.LblKomsulukDegeri_5 = QLabel(Form)
        self.LblKomsulukDegeri_5.setObjectName(u"LblKomsulukDegeri_5")
        self.LblKomsulukDegeri_5.setGeometry(QRect(880, 400, 121, 21))
        self.LblKomsulukDegeri_5.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LblTestOrani.setText(QCoreApplication.translate("Form", u"Test Oran\u0131 :", None))
        self.LblKomsulukDegeri.setText(QCoreApplication.translate("Form", u"Kom\u015fuluk de\u011feri :", None))
        self.TxtEgit.setText(QCoreApplication.translate("Form", u"EGIT", None))
        self.LblAccuracy.setText("")
        self.LblPrecision.setText("")
        self.LblRecall.setText("")
        self.LblF1Score.setText("")
        self.LblSpecificity.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"KNN", None))
        self.label_2.setText("")
        self.LblKomsulukDegeri_2.setText(QCoreApplication.translate("Form", u"X-Test", None))
        self.LblKomsulukDegeri_3.setText(QCoreApplication.translate("Form", u"y-Test", None))
        self.LblKomsulukDegeri_4.setText(QCoreApplication.translate("Form", u"X-Train", None))
        self.LblKomsulukDegeri_5.setText(QCoreApplication.translate("Form", u"y-Train", None))
    # retranslateUi

