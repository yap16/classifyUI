# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1034, 765)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 290, 791, 181))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.image1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image1.setObjectName("image1")
        self.horizontalLayout.addWidget(self.image1)
        self.image2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image2.setObjectName("image2")
        self.horizontalLayout.addWidget(self.image2)
        self.image3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image3.setObjectName("image3")
        self.horizontalLayout.addWidget(self.image3)
        self.image4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image4.setObjectName("image4")
        self.horizontalLayout.addWidget(self.image4)
        self.image5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image5.setObjectName("image5")
        self.horizontalLayout.addWidget(self.image5)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(670, 480, 322, 53))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonGoHome = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.buttonGoHome.setFont(font)
        self.buttonGoHome.setObjectName("buttonGoHome")
        self.horizontalLayout_2.addWidget(self.buttonGoHome)
        self.buttonGoBefore = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.buttonGoBefore.setFont(font)
        self.buttonGoBefore.setObjectName("buttonGoBefore")
        self.horizontalLayout_2.addWidget(self.buttonGoBefore)
        self.buttonGoNext = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.buttonGoNext.setFont(font)
        self.buttonGoNext.setObjectName("buttonGoNext")
        self.horizontalLayout_2.addWidget(self.buttonGoNext)
        self.buttonGoEnd = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.buttonGoEnd.setFont(font)
        self.buttonGoEnd.setObjectName("buttonGoEnd")
        self.horizontalLayout_2.addWidget(self.buttonGoEnd)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(650, 600, 271, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 60, 821, 121))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1034, 17))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.getPath)
        self.buttonGoBefore.clicked.connect(MainWindow.goBefore)
        self.buttonGoNext.clicked.connect(MainWindow.goNext)
        self.buttonGoEnd.clicked.connect(MainWindow.goEnd)
        self.buttonGoHome.clicked.connect(MainWindow.goHome)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image1.setText(_translate("MainWindow", "image1"))
        self.image2.setText(_translate("MainWindow", "image2"))
        self.image3.setText(_translate("MainWindow", "image3"))
        self.image4.setText(_translate("MainWindow", "image4"))
        self.image5.setText(_translate("MainWindow", "image5"))
        self.buttonGoHome.setText(_translate("MainWindow", "<<"))
        self.buttonGoBefore.setText(_translate("MainWindow", "<"))
        self.buttonGoNext.setText(_translate("MainWindow", ">"))
        self.buttonGoEnd.setText(_translate("MainWindow", ">>"))
        self.pushButton_2.setText(_translate("MainWindow", "open fold"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
