# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(916, 766)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 170, 111, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMouseTracking(True)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(180, 120, 541, 471))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.groupBox_1 = QGroupBox(self.Page1)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setGeometry(QRect(0, 0, 541, 111))
        self.title1 = QLabel(self.groupBox_1)
        self.title1.setObjectName(u"title1")
        self.title1.setGeometry(QRect(10, 10, 391, 41))
        font = QFont()
        font.setPointSize(12)
        self.title1.setFont(font)
        self.author1 = QLabel(self.groupBox_1)
        self.author1.setObjectName(u"author1")
        self.author1.setGeometry(QRect(10, 50, 281, 16))
        self.conf1 = QLabel(self.groupBox_1)
        self.conf1.setObjectName(u"conf1")
        self.conf1.setGeometry(QRect(10, 70, 251, 16))
        self.widget_4 = QWidget(self.groupBox_1)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(220, 110, 421, 111))
        self.label_13 = QLabel(self.widget_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 10, 391, 41))
        self.label_13.setFont(font)
        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 50, 281, 16))
        self.label_15 = QLabel(self.widget_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 70, 251, 16))
        self.downloadButton1 = QPushButton(self.groupBox_1)
        self.downloadButton1.setObjectName(u"downloadButton1")
        self.downloadButton1.setGeometry(QRect(330, 80, 75, 24))
        self.paperButton1 = QPushButton(self.groupBox_1)
        self.paperButton1.setObjectName(u"paperButton1")
        self.paperButton1.setGeometry(QRect(430, 80, 75, 24))
        self.groupBox_2 = QGroupBox(self.Page1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 110, 541, 111))
        self.title2 = QLabel(self.groupBox_2)
        self.title2.setObjectName(u"title2")
        self.title2.setGeometry(QRect(10, 10, 391, 41))
        self.title2.setFont(font)
        self.author2 = QLabel(self.groupBox_2)
        self.author2.setObjectName(u"author2")
        self.author2.setGeometry(QRect(10, 50, 281, 16))
        self.conf2 = QLabel(self.groupBox_2)
        self.conf2.setObjectName(u"conf2")
        self.conf2.setGeometry(QRect(10, 70, 251, 16))
        self.widget_5 = QWidget(self.groupBox_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(220, 110, 421, 111))
        self.label_19 = QLabel(self.widget_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 10, 391, 41))
        self.label_19.setFont(font)
        self.label_20 = QLabel(self.widget_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 50, 281, 16))
        self.label_21 = QLabel(self.widget_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 70, 251, 16))
        self.downloadButton2 = QPushButton(self.groupBox_2)
        self.downloadButton2.setObjectName(u"downloadButton2")
        self.downloadButton2.setGeometry(QRect(330, 80, 75, 24))
        self.paperButton2 = QPushButton(self.groupBox_2)
        self.paperButton2.setObjectName(u"paperButton2")
        self.paperButton2.setGeometry(QRect(430, 80, 75, 24))
        self.groupBox_3 = QGroupBox(self.Page1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 220, 541, 111))
        self.title3 = QLabel(self.groupBox_3)
        self.title3.setObjectName(u"title3")
        self.title3.setGeometry(QRect(10, 10, 391, 41))
        self.title3.setFont(font)
        self.author3 = QLabel(self.groupBox_3)
        self.author3.setObjectName(u"author3")
        self.author3.setGeometry(QRect(10, 50, 281, 16))
        self.conf3 = QLabel(self.groupBox_3)
        self.conf3.setObjectName(u"conf3")
        self.conf3.setGeometry(QRect(10, 70, 251, 16))
        self.widget_6 = QWidget(self.groupBox_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(220, 110, 421, 111))
        self.label_25 = QLabel(self.widget_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 10, 391, 41))
        self.label_25.setFont(font)
        self.label_26 = QLabel(self.widget_6)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 50, 281, 16))
        self.label_27 = QLabel(self.widget_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 70, 251, 16))
        self.downloadButton3 = QPushButton(self.groupBox_3)
        self.downloadButton3.setObjectName(u"downloadButton3")
        self.downloadButton3.setGeometry(QRect(330, 80, 75, 24))
        self.paperButton3 = QPushButton(self.groupBox_3)
        self.paperButton3.setObjectName(u"paperButton3")
        self.paperButton3.setGeometry(QRect(430, 80, 75, 24))
        self.groupBox_4 = QGroupBox(self.Page1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 330, 541, 111))
        self.title4 = QLabel(self.groupBox_4)
        self.title4.setObjectName(u"title4")
        self.title4.setGeometry(QRect(10, 10, 391, 41))
        self.title4.setFont(font)
        self.author4 = QLabel(self.groupBox_4)
        self.author4.setObjectName(u"author4")
        self.author4.setGeometry(QRect(10, 50, 281, 16))
        self.conf4 = QLabel(self.groupBox_4)
        self.conf4.setObjectName(u"conf4")
        self.conf4.setGeometry(QRect(10, 70, 251, 16))
        self.widget_7 = QWidget(self.groupBox_4)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(220, 110, 421, 111))
        self.label_31 = QLabel(self.widget_7)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 10, 391, 41))
        self.label_31.setFont(font)
        self.label_32 = QLabel(self.widget_7)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 50, 281, 16))
        self.label_33 = QLabel(self.widget_7)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(10, 70, 251, 16))
        self.downloadButton4 = QPushButton(self.groupBox_4)
        self.downloadButton4.setObjectName(u"downloadButton4")
        self.downloadButton4.setGeometry(QRect(330, 80, 75, 24))
        self.paperButton4 = QPushButton(self.groupBox_4)
        self.paperButton4.setObjectName(u"paperButton4")
        self.paperButton4.setGeometry(QRect(430, 80, 75, 24))
        self.tabWidget.addTab(self.Page1, "")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(140, 40, 581, 80))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 20, 411, 41))
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(520, 20, 61, 41))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(680, 610, 41, 24))
        font1 = QFont()
        font1.setPointSize(15)
        self.pushButton_2.setFont(font1)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(620, 610, 41, 24))
        self.pushButton_3.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 916, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8bba\u6587\u4e0b\u8f7d", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.title1.setText(QCoreApplication.translate("MainWindow", u"Genetic Algorithms and Machine Learning", None))
        self.author1.setText(QCoreApplication.translate("MainWindow", u"David E.Goldberg", None))
        self.conf1.setText(QCoreApplication.translate("MainWindow", u"Machine Learning,(1988)", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Genetic Algorithms and Machine Learning", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"David E.Goldberg", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Machine Learning,(1988)", None))
        self.downloadButton1.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u5168\u6587", None))
        self.paperButton1.setText(QCoreApplication.translate("MainWindow", u"\u6587\u7ae0\u94fe\u63a5", None))
        self.title2.setText(QCoreApplication.translate("MainWindow", u"Genetic Algorithms and Machine Learning", None))
        self.author2.setText(QCoreApplication.translate("MainWindow", u"David E.Goldberg", None))
        self.conf2.setText(QCoreApplication.translate("MainWindow", u"Machine Learning,(1988)", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Genetic Algorithms and Machine Learning", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"David E.Goldberg", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Machine Learning,(1988)", None))
        self.downloadButton2.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u5168\u6587", None))
        self.paperButton2.setText(QCoreApplication.translate("MainWindow", u"\u6587\u7ae0\u94fe\u63a5", None))
        self.title3.setText(QCoreApplication.translate("MainWindow", u"Genetic Algorithms and Machine Learning", None))
        self.author3.setText(QCoreApplication.translate("MainWindow", u"David E.Goldberg", None))
        self.conf3.setText(QCoreApplication.translate("MainWindow", u"Machine Learning,(1988)", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Genetic Algorithms and Machine Learning", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"David E.Goldberg", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Machine Learning,(1988)", None))
        self.downloadButton3.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u5168\u6587", None))
        self.paperButton3.setText(QCoreApplication.translate("MainWindow", u"\u6587\u7ae0\u94fe\u63a5", None))
        self.title4.setText(QCoreApplication.translate("MainWindow", u"Genetic Algorithms and Machine Learning", None))
        self.author4.setText(QCoreApplication.translate("MainWindow", u"David E.Goldberg", None))
        self.conf4.setText(QCoreApplication.translate("MainWindow", u"Machine Learning,(1988)", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Genetic Algorithms and Machine Learning", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"David E.Goldberg", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Machine Learning,(1988)", None))
        self.downloadButton4.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u5168\u6587", None))
        self.paperButton4.setText(QCoreApplication.translate("MainWindow", u"\u6587\u7ae0\u94fe\u63a5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Page1), "")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"<", None))
    # retranslateUi
