# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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
        self.tabWidget.setGeometry(QtCore.QRect(0, -10, 830, 561))
        self.tabWidget.setMinimumSize(QtCore.QSize(830, 561))
        self.tabWidget.setMaximumSize(QtCore.QSize(830, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 30, 281, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEditname = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEditname.setObjectName("lineEditname")
        self.gridLayout.addWidget(self.lineEditname, 0, 1, 1, 1)
        self.linesurname = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.linesurname.setObjectName("linesurname")
        self.gridLayout.addWidget(self.linesurname, 1, 1, 1, 1)
        self.lineage = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineage.setObjectName("lineage")
        self.gridLayout.addWidget(self.lineage, 2, 1, 1, 1)
        self.linebirth = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.linebirth.setObjectName("linebirth")
        self.gridLayout.addWidget(self.linebirth, 3, 1, 1, 1)
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
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(540, 30, 241, 251))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButtonprevious = QtWidgets.QPushButton(self.tab)
        self.pushButtonprevious.setGeometry(QtCore.QRect(500, 460, 121, 31))
        self.pushButtonprevious.setObjectName("pushButtonprevious")
        self.pushButtonnext = QtWidgets.QPushButton(self.tab)
        self.pushButtonnext.setGeometry(QtCore.QRect(660, 460, 121, 31))
        self.pushButtonnext.setObjectName("pushButtonnext")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
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
        self.label_2.setText(_translate("MainWindow", "Прізвище"))
        self.label.setText(_translate("MainWindow", "Ім\'я"))
        self.label_4.setText(_translate("MainWindow", "Рік народження"))
        self.label_3.setText(_translate("MainWindow", "Вік"))
        self.label_5.setText(_translate("MainWindow", "Адреса              "))
        self.label_6.setText(_translate("MainWindow", "Телефон"))
        self.label_8.setText(_translate("MainWindow", "Дата поступлення"))
        self.label_7.setText(_translate("MainWindow", "Палата"))
        self.label_9.setText(_translate("MainWindow", "Дата виписки"))
        self.pushButtonprevious.setText(_translate("MainWindow", "Назад"))
        self.pushButtonnext.setText(_translate("MainWindow", "Вперед"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Пацієнт"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
