# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitledadd.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 590)
        MainWindow.setMinimumSize(QtCore.QSize(830, 590))
        MainWindow.setMaximumSize(QtCore.QSize(830, 590))
        MainWindow.setMouseTracking(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 841, 551))
        self.tabWidget.setMinimumSize(QtCore.QSize(841, 551))
        self.tabWidget.setMaximumSize(QtCore.QSize(841, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 30, 281, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.linesurname = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.linesurname.setObjectName("linesurname")
        self.gridLayout.addWidget(self.linesurname, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineage = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineage.setObjectName("lineage")
        self.gridLayout.addWidget(self.lineage, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditname = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEditname.setObjectName("lineEditname")
        self.gridLayout.addWidget(self.lineEditname, 0, 1, 1, 1)
        self.linebirth = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.linebirth.setObjectName("linebirth")
        self.gridLayout.addWidget(self.linebirth, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 320, 281, 181))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.linechamber = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.linechamber.setObjectName("linechamber")
        self.gridLayout_2.addWidget(self.linechamber, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 1, 1, 1)
        self.linephone = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.linephone.setObjectName("linephone")
        self.gridLayout_2.addWidget(self.linephone, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1)
        self.lineadress = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineadress.setObjectName("lineadress")
        self.gridLayout_2.addWidget(self.lineadress, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 4, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 3, 2, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout_2.addWidget(self.dateEdit_2, 4, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(540, 450, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 450, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.photoLabel = QtWidgets.QLabel(self.tab)
        self.photoLabel.setGeometry(QtCore.QRect(540, 30, 241, 211))
        self.photoLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.photoLabel.setObjectName("photoLabel")
        self.loadphoto = QtWidgets.QPushButton(self.tab)
        self.loadphoto.setGeometry(QtCore.QRect(540, 250, 241, 23))
        self.loadphoto.setObjectName("loadphoto")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 330, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(420, 360, 71, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.clearbutton = QtWidgets.QPushButton(self.tab)
        self.clearbutton.setGeometry(QtCore.QRect(380, 450, 111, 51))
        self.clearbutton.setObjectName("clearbutton")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(90, 250, 241, 31))
        self.comboBox.setObjectName("comboBox")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(540, 320, 241, 91))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.labeldiagnosis = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.labeldiagnosis.setObjectName("labeldiagnosis")
        self.gridLayout_5.addWidget(self.labeldiagnosis, 0, 0, 1, 1)
        self.labeldiagnosisdepartment = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.labeldiagnosisdepartment.setObjectName("labeldiagnosisdepartment")
        self.gridLayout_5.addWidget(self.labeldiagnosisdepartment, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_5.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_5.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(50, 250, 41, 31))
        self.label_18.setObjectName("label_18")
        self.backbutton = QtWidgets.QPushButton(self.tab)
        self.backbutton.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.backbutton.setObjectName("backbutton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.photoLabel_2 = QtWidgets.QLabel(self.tab_2)
        self.photoLabel_2.setGeometry(QtCore.QRect(540, 30, 241, 211))
        self.photoLabel_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.photoLabel_2.setObjectName("photoLabel_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(50, 30, 281, 191))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.lineage_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineage_2.setObjectName("lineage_2")
        self.gridLayout_3.addWidget(self.lineage_2, 2, 1, 1, 1)
        self.linesurname_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.linesurname_2.setObjectName("linesurname_2")
        self.gridLayout_3.addWidget(self.linesurname_2, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.lineEditname_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEditname_2.setObjectName("lineEditname_2")
        self.gridLayout_3.addWidget(self.lineEditname_2, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 3, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 2, 0, 1, 1)
        self.linenumber_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.linenumber_2.setObjectName("linenumber_2")
        self.gridLayout_3.addWidget(self.linenumber_2, 3, 1, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(50, 320, 281, 181))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 4, 1, 1, 1)
        self.linestate_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.linestate_2.setObjectName("linestate_2")
        self.gridLayout_4.addWidget(self.linestate_2, 1, 2, 1, 1)
        self.linesalary_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.linesalary_2.setObjectName("linesalary_2")
        self.gridLayout_4.addWidget(self.linesalary_2, 2, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 2, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 1, 1, 1, 1)
        self.linespeciality_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.linespeciality_2.setObjectName("linespeciality_2")
        self.gridLayout_4.addWidget(self.linespeciality_2, 0, 2, 1, 1)
        self.linedepartment = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.linedepartment.setObjectName("linedepartment")
        self.gridLayout_4.addWidget(self.linedepartment, 4, 2, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hospitalqt"))
        self.label.setText(_translate("MainWindow", "Ім\'я"))
        self.label_3.setText(_translate("MainWindow", "Вік"))
        self.label_2.setText(_translate("MainWindow", "Прізвище"))
        self.label_4.setText(_translate("MainWindow", "Рік народження"))
        self.label_5.setText(_translate("MainWindow", "Адреса              "))
        self.label_6.setText(_translate("MainWindow", "Телефон"))
        self.label_8.setText(_translate("MainWindow", "Дата поступлення"))
        self.label_7.setText(_translate("MainWindow", "Палата"))
        self.label_9.setText(_translate("MainWindow", "Дата виписки"))
        self.pushButton.setText(_translate("MainWindow", "Додати"))
        self.pushButton_2.setText(_translate("MainWindow", "Обновити"))
        self.photoLabel.setText(_translate("MainWindow", "TextLabel"))
        self.loadphoto.setText(_translate("MainWindow", "Завантажити фото"))
        self.pushButton_3.setText(_translate("MainWindow", "test download"))
        self.clearbutton.setText(_translate("MainWindow", "Очистити"))
        self.labeldiagnosis.setText(_translate("MainWindow", "Дігноз"))
        self.labeldiagnosisdepartment.setText(_translate("MainWindow", "Відділення"))
        self.label_18.setText(_translate("MainWindow", "Лікар"))
        self.backbutton.setText(_translate("MainWindow", "Назад"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Пацієнт"))
        self.photoLabel_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "Прізвище"))
        self.label_11.setText(_translate("MainWindow", "Ім\'я"))
        self.label_12.setText(_translate("MainWindow", "Телефон            "))
        self.label_13.setText(_translate("MainWindow", "Вік"))
        self.label_16.setText(_translate("MainWindow", "Відділення"))
        self.label_14.setText(_translate("MainWindow", "Спеціальність    "))
        self.label_17.setText(_translate("MainWindow", "Зарплатня"))
        self.label_15.setText(_translate("MainWindow", "Посада"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Лікар"))