# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guibsufip.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 589)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_frame = QFrame(self.centralwidget)
        self.Top_frame.setObjectName(u"Top_frame")
        self.Top_frame.setMinimumSize(QSize(0, 40))
        self.Top_frame.setMaximumSize(QSize(16777215, 40))
        self.Top_frame.setStyleSheet(u"background-color: rgb(38, 255, 160);\n"
"")
        self.Top_frame.setFrameShape(QFrame.StyledPanel)
        self.Top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Top_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_menu = QPushButton(self.Top_frame)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMinimumSize(QSize(200, 35))
        self.btn_menu.setMaximumSize(QSize(16777215, 35))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_menu.setFont(font)
        self.btn_menu.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid#aa00ff;\n"
"background-color:#ffff00;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../DinamicMenu/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_menu)

        self.horizontalSpacer = QSpacerItem(451, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_minimizar = QPushButton(self.Top_frame)
        self.btn_minimizar.setObjectName(u"btn_minimizar")
        self.btn_minimizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid#aa00ff;\n"
"background-color:#ffff00;\n"
"}")
        self.btn_minimizar.setText(u"")
        icon1 = QIcon()
        icon1.addFile(u"../DinamicMenu/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimizar.setIcon(icon1)
        self.btn_minimizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_minimizar)

        self.btn_restaurar = QPushButton(self.Top_frame)
        self.btn_restaurar.setObjectName(u"btn_restaurar")
        self.btn_restaurar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid#aa00ff;\n"
"background-color:#ffff00;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../DinamicMenu/icons/minimize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_restaurar.setIcon(icon2)
        self.btn_restaurar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_restaurar)

        self.btn_maximizar = QPushButton(self.Top_frame)
        self.btn_maximizar.setObjectName(u"btn_maximizar")
        self.btn_maximizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid#aa00ff;\n"
"background-color:#ffff00;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../DinamicMenu/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximizar.setIcon(icon3)
        self.btn_maximizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_maximizar)

        self.btn_cerrar = QPushButton(self.Top_frame)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        self.btn_cerrar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid#aa00ff;\n"
"background-color:#ffff00;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"../DinamicMenu/icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cerrar.setIcon(icon4)
        self.btn_cerrar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_cerrar)


        self.verticalLayout.addWidget(self.Top_frame)

        self.Bottom_frame = QFrame(self.centralwidget)
        self.Bottom_frame.setObjectName(u"Bottom_frame")
        self.Bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.Bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Bottom_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Lateral_frame = QFrame(self.Bottom_frame)
        self.Lateral_frame.setObjectName(u"Lateral_frame")
        self.Lateral_frame.setEnabled(True)
        self.Lateral_frame.setMinimumSize(QSize(0, 0))
        self.Lateral_frame.setMaximumSize(QSize(0, 16777215))
        self.Lateral_frame.setAutoFillBackground(False)
        self.Lateral_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(38, 255, 208);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #7de5ff;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"\n"
"font: 75 20pt \"Arial Narrow\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"backgroud-color:white;\n"
"border-top.left.radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"font: 75 12pt \"Arial Narrow\";\n"
"\n"
"}")
        self.Lateral_frame.setFrameShape(QFrame.StyledPanel)
        self.Lateral_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Lateral_frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.btn_Home = QPushButton(self.Lateral_frame)
        self.btn_Home.setObjectName(u"btn_Home")
        self.btn_Home.setMinimumSize(QSize(0, 40))
        self.btn_Home.setMaximumSize(QSize(16777215, 40))
        self.btn_Home.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid#aa00ff;\n"
"background-color:#ffff00;\n"
"}\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Home.setIcon(icon5)
        self.btn_Home.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.btn_Home)

        self.btn_Streaming = QPushButton(self.Lateral_frame)
        self.btn_Streaming.setObjectName(u"btn_Streaming")
        self.btn_Streaming.setMinimumSize(QSize(0, 40))
        self.btn_Streaming.setMaximumSize(QSize(16777215, 40))
        self.btn_Streaming.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid#aa00ff;\n"
"background-color:#ffff00;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"../DinamicMenu/icons/eye.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Streaming.setIcon(icon6)
        self.btn_Streaming.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.btn_Streaming)

        self.btn_Bluetooth = QPushButton(self.Lateral_frame)
        self.btn_Bluetooth.setObjectName(u"btn_Bluetooth")
        self.btn_Bluetooth.setMinimumSize(QSize(0, 40))
        self.btn_Bluetooth.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamily(u"Arial Narrow")
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(9)
        self.btn_Bluetooth.setFont(font1)
        self.btn_Bluetooth.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid#aa00ff;\n"
"background-color:#ffff00;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"../DinamicMenu/icons/bluetooth.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Bluetooth.setIcon(icon7)
        self.btn_Bluetooth.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.btn_Bluetooth)

        self.verticalSpacer = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.ad = QLabel(self.Lateral_frame)
        self.ad.setObjectName(u"ad")
        self.ad.setMinimumSize(QSize(181, 141))
        self.ad.setMaximumSize(QSize(181, 141))
        font2 = QFont()
        font2.setFamily(u"Arial Black")
        font2.setPointSize(22)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.ad.setFont(font2)
        self.ad.setStyleSheet(u"")
        self.ad.setTextFormat(Qt.RichText)
        self.ad.setPixmap(QPixmap(u"logonew.png"))
        self.ad.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.ad)


        self.horizontalLayout.addWidget(self.Lateral_frame)

        self.Docker_frame = QFrame(self.Bottom_frame)
        self.Docker_frame.setObjectName(u"Docker_frame")
        self.Docker_frame.setFrameShape(QFrame.StyledPanel)
        self.Docker_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Docker_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.Docker_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Home_page = QWidget()
        self.Home_page.setObjectName(u"Home_page")
        self.gridLayout = QGridLayout(self.Home_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.bg = QLabel(self.Home_page)
        self.bg.setObjectName(u"bg")
        self.bg.setPixmap(QPixmap(u"icons/logoBgWhite.png"))
        self.bg.setScaledContents(True)

        self.gridLayout.addWidget(self.bg, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Home_page)
        self.Streaming_page = QWidget()
        self.Streaming_page.setObjectName(u"Streaming_page")
        self.horizontalLayout_4 = QHBoxLayout(self.Streaming_page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gb_Docker = QGroupBox(self.Streaming_page)
        self.gb_Docker.setObjectName(u"gb_Docker")
        self.gridLayout_2 = QGridLayout(self.gb_Docker)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gb_Skeleton = QGroupBox(self.gb_Docker)
        self.gb_Skeleton.setObjectName(u"gb_Skeleton")
        self.gb_Skeleton.setMinimumSize(QSize(249, 281))
        self.gb_Skeleton.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(12)
        self.gb_Skeleton.setFont(font3)
        self.gridLayout_3 = QGridLayout(self.gb_Skeleton)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lb_Skeleton = QLabel(self.gb_Skeleton)
        self.lb_Skeleton.setObjectName(u"lb_Skeleton")
        self.lb_Skeleton.setPixmap(QPixmap(u"icons/aviso.png"))
        self.lb_Skeleton.setScaledContents(True)

        self.gridLayout_3.addWidget(self.lb_Skeleton, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.gb_Skeleton, 0, 0, 1, 1)

        self.gb_Exercise = QGroupBox(self.gb_Docker)
        self.gb_Exercise.setObjectName(u"gb_Exercise")
        self.gb_Exercise.setMinimumSize(QSize(249, 321))
        self.gb_Exercise.setMaximumSize(QSize(16777215, 16777215))
        self.gb_Exercise.setFont(font3)
        self.gb_Exercise.setFlat(True)
        self.gridLayout_5 = QGridLayout(self.gb_Exercise)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lb_Exercise = QLabel(self.gb_Exercise)
        self.lb_Exercise.setObjectName(u"lb_Exercise")
        font4 = QFont()
        font4.setFamily(u"Cascadia Code SemiBold")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.lb_Exercise.setFont(font4)
        self.lb_Exercise.setStyleSheet(u"background-color: rgb(239, 220, 175);")
        self.lb_Exercise.setTextFormat(Qt.MarkdownText)
        self.lb_Exercise.setWordWrap(True)

        self.gridLayout_5.addWidget(self.lb_Exercise, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.gb_Exercise, 0, 2, 2, 1)

        self.gb_Angles = QGroupBox(self.gb_Docker)
        self.gb_Angles.setObjectName(u"gb_Angles")
        self.gb_Angles.setMaximumSize(QSize(16777215, 16777215))
        self.gb_Angles.setFont(font3)
        self.gb_Angles.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_8 = QGridLayout(self.gb_Angles)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_3 = QLabel(self.gb_Angles)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(117, 21))
        self.label_3.setMaximumSize(QSize(117, 21))

        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_7 = QLabel(self.gb_Angles)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(109, 16))
        self.label_7.setMaximumSize(QSize(109, 16))

        self.gridLayout_8.addWidget(self.label_7, 0, 1, 1, 1)

        self.lb_RAA = QLabel(self.gb_Angles)
        self.lb_RAA.setObjectName(u"lb_RAA")
        self.lb_RAA.setMinimumSize(QSize(47, 13))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.lb_RAA.setFont(font5)

        self.gridLayout_8.addWidget(self.lb_RAA, 1, 0, 1, 1)

        self.lb_LAA = QLabel(self.gb_Angles)
        self.lb_LAA.setObjectName(u"lb_LAA")
        self.lb_LAA.setFont(font5)

        self.gridLayout_8.addWidget(self.lb_LAA, 1, 1, 1, 1)

        self.label_4 = QLabel(self.gb_Angles)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(147, 16))
        self.label_4.setMaximumSize(QSize(147, 16))

        self.gridLayout_8.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_6 = QLabel(self.gb_Angles)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(139, 16))
        self.label_6.setMaximumSize(QSize(139, 16))

        self.gridLayout_8.addWidget(self.label_6, 2, 1, 1, 1)

        self.lb_RSA = QLabel(self.gb_Angles)
        self.lb_RSA.setObjectName(u"lb_RSA")
        self.lb_RSA.setFont(font5)

        self.gridLayout_8.addWidget(self.lb_RSA, 3, 0, 1, 1)

        self.lb_LSA = QLabel(self.gb_Angles)
        self.lb_LSA.setObjectName(u"lb_LSA")
        self.lb_LSA.setFont(font5)

        self.gridLayout_8.addWidget(self.lb_LSA, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.gb_Angles, 2, 0, 1, 2)

        self.gb_Emotion = QGroupBox(self.gb_Docker)
        self.gb_Emotion.setObjectName(u"gb_Emotion")
        self.gb_Emotion.setMinimumSize(QSize(248, 281))
        self.gb_Emotion.setMaximumSize(QSize(16777215, 16777215))
        self.gb_Emotion.setFont(font3)
        self.gridLayout_4 = QGridLayout(self.gb_Emotion)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lb_Emotion = QLabel(self.gb_Emotion)
        self.lb_Emotion.setObjectName(u"lb_Emotion")
        self.lb_Emotion.setPixmap(QPixmap(u"icons/aviso.png"))
        self.lb_Emotion.setScaledContents(True)

        self.gridLayout_4.addWidget(self.lb_Emotion, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.gb_Emotion, 0, 1, 1, 1)

        self.gb_Linke = QGroupBox(self.gb_Docker)
        self.gb_Linke.setObjectName(u"gb_Linke")
        self.gb_Linke.setMaximumSize(QSize(249, 163))
        self.gb_Linke.setFont(font3)
        self.gb_Linke.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.gb_Linke.setFlat(True)
        self.gridLayout_9 = QGridLayout(self.gb_Linke)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_9 = QLabel(self.gb_Linke)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(61, 101))
        self.label_9.setMaximumSize(QSize(61, 101))
        self.label_9.setPixmap(QPixmap(u"blutwo.png"))
        self.label_9.setScaledContents(True)

        self.gridLayout_9.addWidget(self.label_9, 0, 0, 1, 1)

        self.lb_vin = QLabel(self.gb_Linke)
        self.lb_vin.setObjectName(u"lb_vin")
        self.lb_vin.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.lb_vin, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.gb_Linke, 2, 2, 1, 1)

        self.gb_States = QGroupBox(self.gb_Docker)
        self.gb_States.setObjectName(u"gb_States")
        self.gb_States.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_7 = QGridLayout(self.gb_States)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.btn_TurnOn = QPushButton(self.gb_States)
        self.btn_TurnOn.setObjectName(u"btn_TurnOn")
        self.btn_TurnOn.setFont(font3)
        self.btn_TurnOn.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(170, 255, 127);\n"
"\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid#aa00ff;\n"
"background-color:#ffff00;\n"
"}\n"
"\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"icons/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_TurnOn.setIcon(icon8)
        self.btn_TurnOn.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.btn_TurnOn, 0, 0, 1, 1)

        self.btn_TurnOff = QPushButton(self.gb_States)
        self.btn_TurnOff.setObjectName(u"btn_TurnOff")
        self.btn_TurnOff.setFont(font3)
        self.btn_TurnOff.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 85, 0);\n"
"\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid#aa00ff;\n"
"background-color:#ffff00;\n"
"}\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"icons/video-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_TurnOff.setIcon(icon9)
        self.btn_TurnOff.setIconSize(QSize(23, 24))

        self.gridLayout_7.addWidget(self.btn_TurnOff, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.gb_States, 1, 0, 1, 2)


        self.horizontalLayout_4.addWidget(self.gb_Docker)

        self.stackedWidget.addWidget(self.Streaming_page)
        self.Connection_page = QWidget()
        self.Connection_page.setObjectName(u"Connection_page")
        self.gridLayout_6 = QGridLayout(self.Connection_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gb_Docker_2 = QGroupBox(self.Connection_page)
        self.gb_Docker_2.setObjectName(u"gb_Docker_2")
        font6 = QFont()
        font6.setPointSize(16)
        self.gb_Docker_2.setFont(font6)
        self.gb_Docker_2.setStyleSheet(u"background-color: rgb(12, 12, 12);")
        self.gridLayout_10 = QGridLayout(self.gb_Docker_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_14 = QLabel(self.gb_Docker_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(391, 31))
        self.label_14.setMaximumSize(QSize(391, 31))
        self.label_14.setFont(font6)

        self.gridLayout_10.addWidget(self.label_14, 0, 0, 1, 2)

        self.cb_Devices = QComboBox(self.gb_Docker_2)
        self.cb_Devices.setObjectName(u"cb_Devices")
        self.cb_Devices.setMinimumSize(QSize(581, 41))
        self.cb_Devices.setMaximumSize(QSize(581, 41))
        self.cb_Devices.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_10.addWidget(self.cb_Devices, 1, 0, 1, 2)

        self.label_15 = QLabel(self.gb_Docker_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(91, 111))
        self.label_15.setMaximumSize(QSize(91, 111))
        self.label_15.setPixmap(QPixmap(u"blutwo.png"))
        self.label_15.setScaledContents(True)

        self.gridLayout_10.addWidget(self.label_15, 2, 0, 1, 1)

        self.lb_VinID = QLabel(self.gb_Docker_2)
        self.lb_VinID.setObjectName(u"lb_VinID")
        self.lb_VinID.setMinimumSize(QSize(181, 41))
        self.lb_VinID.setMaximumSize(QSize(181, 41))
        self.lb_VinID.setFont(font6)
        self.lb_VinID.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.lb_VinID, 2, 1, 1, 1)

        self.btn_Pair = QPushButton(self.gb_Docker_2)
        self.btn_Pair.setObjectName(u"btn_Pair")
        self.btn_Pair.setMinimumSize(QSize(181, 71))
        self.btn_Pair.setMaximumSize(QSize(181, 71))
        self.btn_Pair.setFont(font6)
        self.btn_Pair.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 255,255);\n"
"\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid#aa00ff;\n"
"background-color:#ffff00;\n"
"}\n"
"\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"icons/phone.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Pair.setIcon(icon10)
        self.btn_Pair.setIconSize(QSize(32, 32))

        self.gridLayout_10.addWidget(self.btn_Pair, 3, 0, 1, 1)

        self.btn_Unpair = QPushButton(self.gb_Docker_2)
        self.btn_Unpair.setObjectName(u"btn_Unpair")
        self.btn_Unpair.setMinimumSize(QSize(181, 71))
        self.btn_Unpair.setMaximumSize(QSize(181, 71))
        self.btn_Unpair.setFont(font6)
        self.btn_Unpair.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 255,255);\n"
"\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid#aa00ff;\n"
"background-color:#ffff00;\n"
"}\n"
"\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"icons/phone-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Unpair.setIcon(icon11)
        self.btn_Unpair.setIconSize(QSize(32, 32))

        self.gridLayout_10.addWidget(self.btn_Unpair, 3, 1, 1, 1)


        self.gridLayout_6.addWidget(self.gb_Docker_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Connection_page)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.Docker_frame)


        self.verticalLayout.addWidget(self.Bottom_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u" MENU", None))
        self.btn_restaurar.setText("")
        self.btn_maximizar.setText("")
        self.btn_Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_Streaming.setText(QCoreApplication.translate("MainWindow", u"Streaming", None))
        self.btn_Bluetooth.setText(QCoreApplication.translate("MainWindow", u"Bluetooth", None))
        self.ad.setText("")
        self.bg.setText("")
        self.gb_Docker.setTitle("")
        self.gb_Skeleton.setTitle(QCoreApplication.translate("MainWindow", u"Skeleton", None))
        self.lb_Skeleton.setText("")
        self.gb_Exercise.setTitle(QCoreApplication.translate("MainWindow", u"Exercise", None))
        self.lb_Exercise.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt; font-weight:600;\">Seleccione un ejercicio desde la aplicaci\u00f3n movil y envielo</span></p></body></html>", None))
        self.gb_Angles.setTitle(QCoreApplication.translate("MainWindow", u"Arm's Angles", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#c7211b;\">Right Arm's Angle</span></p><p><br/></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#c7211b;\">Left Arm's Angle</span></p><p><br/></p></body></html>", None))
        self.lb_RAA.setText(QCoreApplication.translate("MainWindow", u"0\u00b0", None))
        self.lb_LAA.setText(QCoreApplication.translate("MainWindow", u"0\u00b0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#c7211b;\">Right Shoulder's Angle</span></p><p><br/></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#c7211b;\">Left Shoulder's Angle</span></p><p><br/></p></body></html>", None))
        self.lb_RSA.setText(QCoreApplication.translate("MainWindow", u"0\u00b0", None))
        self.lb_LSA.setText(QCoreApplication.translate("MainWindow", u"0\u00b0", None))
        self.gb_Emotion.setTitle(QCoreApplication.translate("MainWindow", u"Emotion", None))
        self.lb_Emotion.setText("")
        self.gb_Linke.setTitle("")
        self.label_9.setText("")
        self.lb_vin.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">No Vinculado</span></p></body></html>", None))
        self.gb_States.setTitle("")
        self.btn_TurnOn.setText(QCoreApplication.translate("MainWindow", u"    Encender Video", None))
        self.btn_TurnOff.setText(QCoreApplication.translate("MainWindow", u"    Apagar Video", None))
        self.gb_Docker_2.setTitle("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Select Bluetooth Device</span></p></body></html>", None))
        self.label_15.setText("")
        self.lb_VinID.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">No Vinculado</span></p></body></html>", None))
        self.btn_Pair.setText(QCoreApplication.translate("MainWindow", u"Pair Device", None))
        self.btn_Unpair.setText(QCoreApplication.translate("MainWindow", u"Unpair Device", None))
    # retranslateUi

