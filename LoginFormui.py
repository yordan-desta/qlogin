# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/pyordan/New Volume/WORK/testProjects/LogInform/loginFormui.ui'
#
# Created: Wed Mar  4 14:50:06 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_loginFormMain(object):
    def setupUi(self, loginFormMain):
        loginFormMain.setObjectName(_fromUtf8("loginFormMain"))
        loginFormMain.resize(400, 233)
        self.username_label = QtGui.QLabel(loginFormMain)
        self.username_label.setGeometry(QtCore.QRect(50, 70, 69, 17))
        self.username_label.setObjectName(_fromUtf8("username_label"))
        self.password_label = QtGui.QLabel(loginFormMain)
        self.password_label.setGeometry(QtCore.QRect(50, 110, 66, 17))
        self.password_label.setObjectName(_fromUtf8("password_label"))
        self.login_button = QtGui.QPushButton(loginFormMain)
        self.login_button.setGeometry(QtCore.QRect(160, 180, 98, 27))
        self.login_button.setObjectName(_fromUtf8("login_button"))
        self.cancel_button = QtGui.QPushButton(loginFormMain)
        self.cancel_button.setGeometry(QtCore.QRect(270, 180, 98, 27))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.username = QtGui.QLineEdit(loginFormMain)
        self.username.setGeometry(QtCore.QRect(120, 60, 251, 31))
        self.username.setObjectName(_fromUtf8("username"))
        self.password = QtGui.QLineEdit(loginFormMain)
        self.password.setGeometry(QtCore.QRect(120, 100, 251, 31))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.status_label = QtGui.QLabel(loginFormMain)
        self.status_label.setGeometry(QtCore.QRect(50, 150, 221, 20))
        self.status_label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.status_label.setTextFormat(QtCore.Qt.RichText)
        self.status_label.setObjectName(_fromUtf8("status_label"))

        self.retranslateUi(loginFormMain)
        QtCore.QMetaObject.connectSlotsByName(loginFormMain)
        loginFormMain.setTabOrder(self.username, self.password)
        loginFormMain.setTabOrder(self.password, self.login_button)
        loginFormMain.setTabOrder(self.login_button, self.cancel_button)

    def retranslateUi(self, loginFormMain):
        loginFormMain.setWindowTitle(_translate("loginFormMain", "LogIn", None))
        self.username_label.setText(_translate("loginFormMain", "Username", None))
        self.password_label.setText(_translate("loginFormMain", "password", None))
        self.login_button.setText(_translate("loginFormMain", "login", None))
        self.cancel_button.setText(_translate("loginFormMain", "cancel", None))
        self.username.setPlaceholderText(_translate("loginFormMain", "Enter your user name", None))
        self.password.setPlaceholderText(_translate("loginFormMain", "Enter your Password", None))
        self.status_label.setText(_translate("loginFormMain", "<html><head/><body><p><br/></p></body></html>", None))

