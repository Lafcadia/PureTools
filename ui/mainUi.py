# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\zhengwanlun\Desktop\Python\Izanagi\ui\mainUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1102, 576)
        MainWindow.setMaximumSize(QtCore.QSize(1102, 576))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.JumpToBilibili = PushButton(self.centralwidget)
        self.JumpToBilibili.setGeometry(QtCore.QRect(680, 190, 191, 41))
        self.JumpToBilibili.setObjectName("JumpToBilibili")
        self.TitleLabel = TitleLabel(self.centralwidget)
        self.TitleLabel.setGeometry(QtCore.QRect(680, 140, 271, 38))
        self.TitleLabel.setObjectName("TitleLabel")
        self.JumpToNetEase = PushButton(self.centralwidget)
        self.JumpToNetEase.setGeometry(QtCore.QRect(680, 240, 191, 41))
        self.JumpToNetEase.setObjectName("JumpToNetEase")
        self.JumpToWallpaper = PushButton(self.centralwidget)
        self.JumpToWallpaper.setGeometry(QtCore.QRect(680, 290, 191, 41))
        self.JumpToWallpaper.setObjectName("JumpToWallpaper")
        self.JumpToRandom = PushButton(self.centralwidget)
        self.JumpToRandom.setGeometry(QtCore.QRect(680, 340, 191, 41))
        self.JumpToRandom.setObjectName("JumpToRandom")
        self.JumpToSongInfo = PushButton(self.centralwidget)
        self.JumpToSongInfo.setGeometry(QtCore.QRect(890, 290, 191, 41))
        self.JumpToSongInfo.setObjectName("JumpToSongInfo")
        self.JumpToConvert = PushButton(self.centralwidget)
        self.JumpToConvert.setGeometry(QtCore.QRect(890, 240, 191, 41))
        self.JumpToConvert.setObjectName("JumpToConvert")
        self.JumpToEncrypt = PushButton(self.centralwidget)
        self.JumpToEncrypt.setGeometry(QtCore.QRect(890, 190, 191, 41))
        self.JumpToEncrypt.setObjectName("JumpToEncrypt")
        self.PixmapLabel = PixmapLabel(self.centralwidget)
        self.PixmapLabel.setGeometry(QtCore.QRect(-10, -10, 641, 601))
        self.PixmapLabel.setAutoFillBackground(False)
        self.PixmapLabel.setScaledContents(True)
        self.PixmapLabel.setObjectName("PixmapLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Izanagi Tools"))
        self.JumpToBilibili.setText(_translate("MainWindow", "Download from Bilibili"))
        self.TitleLabel.setText(_translate("MainWindow", "Izanagi Tools - v0.0.1"))
        self.JumpToNetEase.setText(_translate("MainWindow", "Download from NetEase"))
        self.JumpToWallpaper.setText(_translate("MainWindow", "Auto Genshin Wallpaper"))
        self.JumpToRandom.setText(_translate("MainWindow", "Pick a Random Choice"))
        self.JumpToSongInfo.setText(_translate("MainWindow", "Modify Song Info"))
        self.JumpToConvert.setText(_translate("MainWindow", "Music/Video Convert"))
        self.JumpToEncrypt.setText(_translate("MainWindow", "Encrypt Files"))
from qfluentwidgets import PixmapLabel, PushButton, TitleLabel
