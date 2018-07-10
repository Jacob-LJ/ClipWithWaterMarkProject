# coding=utf-8

from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget, QListWidget, QWidget, QLineEdit, QDateTimeEdit, QVBoxLayout, QHBoxLayout \
        , QGridLayout, QLabel
from PyQt5.QtCore import Qt, QDateTime
import Utils
import os

# 应用程序的主Widget
class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vlayout = QVBoxLayout()
        grid = QGridLayout()
        label1 = QLabel('文件路径')
        self.lineEdit = QLineEdit()
        label2 = QLabel('时间点')
        self.dateEdit = QDateTimeEdit()
        self.dateEdit.setDisplayFormat('yyyy-MM-dd hh:mm:ss')
        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.lineEdit, 0, 1, )
        grid.addWidget(label2, 1, 0)
        grid.addWidget(self.dateEdit, 1, 1)
        vlayout.addLayout(grid)
        vlayout.addStretch(1)
        self.setLayout(vlayout)


    def onClipboradChanged(self):
        clipboard = QApplication.clipboard()
        text = clipboard.text()
        if text:
            content = str(text)
            print('onClipboradChanged---' + content + ' len = ' + str(len(content)))
            if content.startswith('file:///'):
                path = content.replace('file:///', '')
                if not os.path.exists(path):
                    return
                name = Utils.fileName(path)
                self.lineEdit.setText(path)
                if Utils.isAllowConvert2Time(name):
                    self.updateDateTimeEdit(filename=name)
                    pass
            elif len(content) < 50:
                self.updateDateTimeEdit(content=content)


    def updateDateTimeEdit(self, filename = '', content = ''):
        if filename:
            times = Utils.extractTimeFromFile(filename)
        elif content:
            times = Utils.extractTime(content)
        if times == -1:
            return
        timestr = Utils.convertSeconds2TimeStr(times)
        print(timestr)
        self.dateEdit.setDateTime(QDateTime.fromString(timestr, 'yyyy-MM-dd hh:mm:ss'))
        pass