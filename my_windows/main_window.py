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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(846, 766)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 170, 111, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"    background-color:rgb(255, 255, 127);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(255, 255, 127);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"    background-color:rgb(255, 255, 127);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(255, 255, 127);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(190, 50, 581, 661))
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName(u"stackedWidgetPage1")
        self.groupBox_1 = QGroupBox(self.stackedWidgetPage1)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setGeometry(QRect(10, 130, 541, 111))
        self.title1 = QLabel(self.groupBox_1)
        self.title1.setObjectName(u"title1")
        self.title1.setGeometry(QRect(10, 10, 531, 41))
        font = QFont()
        font.setPointSize(11)
        self.title1.setFont(font)
        self.title1.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.author1 = QLabel(self.groupBox_1)
        self.author1.setObjectName(u"author1")
        self.author1.setGeometry(QRect(10, 50, 501, 16))
        self.conf1 = QLabel(self.groupBox_1)
        self.conf1.setObjectName(u"conf1")
        self.conf1.setGeometry(QRect(10, 70, 251, 16))
        self.widget_4 = QWidget(self.groupBox_1)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(220, 110, 421, 111))
        self.label_13 = QLabel(self.widget_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 10, 391, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_13.setFont(font1)
        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 50, 281, 16))
        self.label_15 = QLabel(self.widget_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 70, 251, 16))
        self.paperButton1 = QPushButton(self.groupBox_1)
        self.paperButton1.setObjectName(u"paperButton1")
        self.paperButton1.setGeometry(QRect(430, 80, 75, 24))
        self.groupBox_2 = QGroupBox(self.stackedWidgetPage1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 250, 541, 111))
        self.title2 = QLabel(self.groupBox_2)
        self.title2.setObjectName(u"title2")
        self.title2.setGeometry(QRect(10, 10, 531, 41))
        self.title2.setFont(font)
        self.title2.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.author2 = QLabel(self.groupBox_2)
        self.author2.setObjectName(u"author2")
        self.author2.setGeometry(QRect(10, 50, 521, 16))
        self.conf2 = QLabel(self.groupBox_2)
        self.conf2.setObjectName(u"conf2")
        self.conf2.setGeometry(QRect(10, 70, 251, 16))
        self.widget_5 = QWidget(self.groupBox_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(220, 110, 421, 111))
        self.label_19 = QLabel(self.widget_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 10, 391, 41))
        self.label_19.setFont(font1)
        self.label_20 = QLabel(self.widget_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 50, 281, 16))
        self.label_21 = QLabel(self.widget_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 70, 251, 16))
        self.paperButton2 = QPushButton(self.groupBox_2)
        self.paperButton2.setObjectName(u"paperButton2")
        self.paperButton2.setGeometry(QRect(430, 80, 75, 24))
        self.groupBox_3 = QGroupBox(self.stackedWidgetPage1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 370, 541, 111))
        self.title3 = QLabel(self.groupBox_3)
        self.title3.setObjectName(u"title3")
        self.title3.setGeometry(QRect(10, 10, 531, 41))
        self.title3.setFont(font)
        self.title3.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.author3 = QLabel(self.groupBox_3)
        self.author3.setObjectName(u"author3")
        self.author3.setGeometry(QRect(10, 50, 521, 16))
        self.conf3 = QLabel(self.groupBox_3)
        self.conf3.setObjectName(u"conf3")
        self.conf3.setGeometry(QRect(10, 70, 251, 16))
        self.widget_6 = QWidget(self.groupBox_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(220, 110, 421, 111))
        self.label_25 = QLabel(self.widget_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 10, 391, 41))
        self.label_25.setFont(font1)
        self.label_26 = QLabel(self.widget_6)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 50, 281, 16))
        self.label_27 = QLabel(self.widget_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 70, 251, 16))
        self.paperButton3 = QPushButton(self.groupBox_3)
        self.paperButton3.setObjectName(u"paperButton3")
        self.paperButton3.setGeometry(QRect(430, 80, 75, 24))
        self.groupBox_4 = QGroupBox(self.stackedWidgetPage1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 490, 541, 111))
        self.title4 = QLabel(self.groupBox_4)
        self.title4.setObjectName(u"title4")
        self.title4.setGeometry(QRect(10, 10, 531, 41))
        self.title4.setFont(font)
        self.title4.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.author4 = QLabel(self.groupBox_4)
        self.author4.setObjectName(u"author4")
        self.author4.setGeometry(QRect(10, 50, 521, 16))
        self.conf4 = QLabel(self.groupBox_4)
        self.conf4.setObjectName(u"conf4")
        self.conf4.setGeometry(QRect(10, 70, 251, 16))
        self.widget_7 = QWidget(self.groupBox_4)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(220, 110, 421, 111))
        self.label_31 = QLabel(self.widget_7)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 10, 391, 41))
        self.label_31.setFont(font1)
        self.label_32 = QLabel(self.widget_7)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 50, 281, 16))
        self.label_33 = QLabel(self.widget_7)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(10, 70, 251, 16))
        self.paperButton4 = QPushButton(self.groupBox_4)
        self.paperButton4.setObjectName(u"paperButton4")
        self.paperButton4.setGeometry(QRect(430, 80, 75, 24))
        self.pushButton_3 = QPushButton(self.stackedWidgetPage1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(450, 610, 41, 24))
        font2 = QFont()
        font2.setPointSize(15)
        self.pushButton_3.setFont(font2)
        self.pushButton_2 = QPushButton(self.stackedWidgetPage1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(500, 610, 41, 24))
        self.pushButton_2.setFont(font2)
        self.lineEdit = QLineEdit(self.stackedWidgetPage1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 60, 411, 41))
        self.pushButton = QPushButton(self.stackedWidgetPage1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(470, 60, 61, 41))
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QWidget()
        self.stackedWidgetPage2.setObjectName(u"stackedWidgetPage2")
        self.stackedWidget.addWidget(self.stackedWidgetPage2)
        self.stackedWidgetPage3 = QWidget()
        self.stackedWidgetPage3.setObjectName(u"stackedWidgetPage3")
        self.pushButton_7 = QPushButton(self.stackedWidgetPage3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(470, 60, 61, 41))
        self.lineEdit_2 = QLineEdit(self.stackedWidgetPage3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 60, 411, 41))
        self.tableWidget = QTableWidget(self.stackedWidgetPage3)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 130, 541, 461))
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.pushButton_8 = QPushButton(self.stackedWidgetPage3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(400, 60, 41, 41))
        self.stackedWidget.addWidget(self.stackedWidgetPage3)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(730, 30, 31, 24))
        self.pushButton_5.setStyleSheet(u"QPushButton\n"
"{\n"
"font-family:\"Webdings\";\n"
"background:#F76677;border-radius:5px;\n"
"border:none;\n"
"font-size:13px;\n"
"}\n"
"QPushButton:hover{background:red;}\n"
"\n"
"\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"pic/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 846, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_5.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u6587\u732e\u68c0\u7d22", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u8003\u6587\u732e\u4e0b\u8f7d", None))
        self.title1.setText(QCoreApplication.translate("MainWindow", u"Genetic Algorithms and Machine Learning", None))
        self.author1.setText(QCoreApplication.translate("MainWindow", u"David E.Goldberg", None))
        self.conf1.setText(QCoreApplication.translate("MainWindow", u"Machine Learning,(1988)", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Genetic Algorithms and Machine Learning", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"David E.Goldberg", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Machine Learning,(1988)", None))
        self.paperButton1.setText(QCoreApplication.translate("MainWindow", u"\u6587\u7ae0\u94fe\u63a5", None))
        self.title2.setText(QCoreApplication.translate("MainWindow", u"Genetic Algorithms and Machine Learning", None))
        self.author2.setText(QCoreApplication.translate("MainWindow", u"David E.Goldberg", None))
        self.conf2.setText(QCoreApplication.translate("MainWindow", u"Machine Learning,(1988)", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Genetic Algorithms and Machine Learning", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"David E.Goldberg", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Machine Learning,(1988)", None))
        self.paperButton2.setText(QCoreApplication.translate("MainWindow", u"\u6587\u7ae0\u94fe\u63a5", None))
        self.title3.setText(QCoreApplication.translate("MainWindow", u"Genetic Algorithms and Machine Learning", None))
        self.author3.setText(QCoreApplication.translate("MainWindow", u"David E.Goldberg", None))
        self.conf3.setText(QCoreApplication.translate("MainWindow", u"Machine Learning,(1988)", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Genetic Algorithms and Machine Learning", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"David E.Goldberg", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Machine Learning,(1988)", None))
        self.paperButton3.setText(QCoreApplication.translate("MainWindow", u"\u6587\u7ae0\u94fe\u63a5", None))
        self.title4.setText(QCoreApplication.translate("MainWindow", u"Genetic Algorithms and Machine Learning", None))
        self.author4.setText(QCoreApplication.translate("MainWindow", u"David E.Goldberg", None))
        self.conf4.setText(QCoreApplication.translate("MainWindow", u"Machine Learning,(1988)", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Genetic Algorithms and Machine Learning", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"David E.Goldberg", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Machine Learning,(1988)", None))
        self.paperButton4.setText(QCoreApplication.translate("MainWindow", u"\u6587\u7ae0\u94fe\u63a5", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u8003\u6587\u732e\u540d\u79f0", None));
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.pushButton_5.setText("")
    # retranslateUi

