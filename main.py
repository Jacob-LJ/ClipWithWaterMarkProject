# coding=utf-8

import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget, QListWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QClipboard
from widgets import MainWidget
import Utils

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()
        self.addClipbordListener()


    def addClipbordListener(self):
        clipboard = QApplication.clipboard()
        clipboard.dataChanged.connect(self.widget.onClipboradChanged)


    def init(self):
        self.text = QTextEdit('主窗口')
        self.widget = MainWidget()
        self.setCentralWidget(self.widget)
        self.setGeometry(200, 200, 800, 400)
        self.setWindowTitle('监听粘贴板')
        self.show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

def test():
    timestramp = Utils.extractTime('2017-6-12 12:24:56')
    times = time.localtime(timestramp)
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", times)
    print(now_time)



# 入口
if __name__ == '__main__':
    test()