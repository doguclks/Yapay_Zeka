# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decision_tree.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1119, 715)
        self.veri_egit = QtWidgets.QPushButton(Form)
        self.veri_egit.setGeometry(QtCore.QRect(460, 400, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.veri_egit.setFont(font)
        self.veri_egit.setObjectName("veri_egit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(470, 170, 151, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.girisli_egit = QtWidgets.QPushButton(Form)
        self.girisli_egit.setGeometry(QtCore.QRect(1000, 90, 93, 28))
        self.girisli_egit.setObjectName("girisli_egit")
        self.TxtAgacDerinligi = QtWidgets.QLineEdit(Form)
        self.TxtAgacDerinligi.setGeometry(QtCore.QRect(840, 90, 113, 22))
        self.TxtAgacDerinligi.setObjectName("TxtAgacDerinligi")
        self.radio_optm = QtWidgets.QRadioButton(Form)
        self.radio_optm.setGeometry(QtCore.QRect(540, 40, 95, 20))
        self.radio_optm.setObjectName("radio_optm")
        self.radio_verigir = QtWidgets.QRadioButton(Form)
        self.radio_verigir.setGeometry(QtCore.QRect(540, 90, 101, 20))
        self.radio_verigir.setObjectName("radio_verigir")
        self.LblAgacDerinligi = QtWidgets.QLabel(Form)
        self.LblAgacDerinligi.setGeometry(QtCore.QRect(710, 90, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LblAgacDerinligi.setFont(font)
        self.LblAgacDerinligi.setObjectName("LblAgacDerinligi")
        self.BtnDYukle = QtWidgets.QPushButton(Form)
        self.BtnDYukle.setGeometry(QtCore.QRect(50, 540, 151, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BtnDYukle.setFont(font)
        self.BtnDYukle.setObjectName("BtnDYukle")
        self.LblDeneme = QtWidgets.QLabel(Form)
        self.LblDeneme.setGeometry(QtCore.QRect(370, 530, 371, 51))
        self.LblDeneme.setObjectName("LblDeneme")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(15, 141, 391, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.optimum_egit = QtWidgets.QPushButton(Form)
        self.optimum_egit.setGeometry(QtCore.QRect(1000, 40, 93, 28))
        self.optimum_egit.setObjectName("optimum_egit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.veri_egit.setText(_translate("Form", "SATIR EGIT"))
        self.pushButton.setText(_translate("Form", "SATIR GETIR"))
        self.girisli_egit.setText(_translate("Form", "EGIT"))
        self.radio_optm.setText(_translate("Form", "OPTIMUM"))
        self.radio_verigir.setText(_translate("Form", "VERI GIRISLI"))
        self.LblAgacDerinligi.setText(_translate("Form", "Ağaç Derinliği"))
        self.BtnDYukle.setText(_translate("Form", "DATASET YUKLE"))
        self.LblDeneme.setText(_translate("Form", "TextLabel"))
        self.label.setText(_translate("Form", "Veri setini optimum(kullanıcı girişi olmadan) eğitmek için tıklayın"))
        self.label_2.setText(_translate("Form", "Kullanıcı girişli eğitim için tıklayın"))
        self.optimum_egit.setText(_translate("Form", "EGIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())