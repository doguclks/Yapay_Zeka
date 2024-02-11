# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ANN_arayuz.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(818, 616)
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
        self.TxtKFold = QLineEdit(Form)
        self.TxtKFold.setObjectName(u"TxtKFold")
        self.TxtKFold.setGeometry(QRect(160, 40, 131, 22))
        self.TxtTestSize = QLineEdit(Form)
        self.TxtTestSize.setObjectName(u"TxtTestSize")
        self.TxtTestSize.setGeometry(QRect(160, 80, 131, 22))
        self.TxtBatchSize = QLineEdit(Form)
        self.TxtBatchSize.setObjectName(u"TxtBatchSize")
        self.TxtBatchSize.setGeometry(QRect(160, 120, 131, 22))
        self.TxtEpochs = QLineEdit(Form)
        self.TxtEpochs.setObjectName(u"TxtEpochs")
        self.TxtEpochs.setGeometry(QRect(160, 160, 131, 22))
        self.TxtValidatioin = QLineEdit(Form)
        self.TxtValidatioin.setObjectName(u"TxtValidatioin")
        self.TxtValidatioin.setGeometry(QRect(160, 200, 131, 22))
        self.TxtPatience = QLineEdit(Form)
        self.TxtPatience.setObjectName(u"TxtPatience")
        self.TxtPatience.setGeometry(QRect(160, 240, 131, 22))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 40, 81, 21))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 80, 81, 21))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 120, 81, 21))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 160, 81, 21))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 200, 101, 21))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 240, 81, 21))
        self.BtnModeliEgit = QPushButton(Form)
        self.BtnModeliEgit.setObjectName(u"BtnModeliEgit")
        self.BtnModeliEgit.setGeometry(QRect(160, 280, 131, 51))
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(380, 20, 311, 81))
        font = QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(380, 130, 311, 71))
        self.label_8.setFont(font)
        QWidget.setTabOrder(self.TxtKFold, self.TxtTestSize)
        QWidget.setTabOrder(self.TxtTestSize, self.TxtBatchSize)
        QWidget.setTabOrder(self.TxtBatchSize, self.TxtEpochs)
        QWidget.setTabOrder(self.TxtEpochs, self.TxtValidatioin)
        QWidget.setTabOrder(self.TxtValidatioin, self.TxtPatience)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TxtTestSize.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"K-Fold", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Test_size:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Batch_size:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Epochs:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Validation_split:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Patience", None))
        self.BtnModeliEgit.setText(QCoreApplication.translate("Form", u"MODELI EGIT", None))
        self.label_7.setText("")
        self.label_8.setText("")
    # retranslateUi

