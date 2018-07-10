
import os
import sys
import re
from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel, QPushButton,)


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # 创建btn 和 label
        textCopyButton = QPushButton("&添加水印", self)
        textCopyButton.clicked.connect(self.btnClick)
        textLabel = QLabel("点击按钮 为剪贴板中图片添加水印")

        # 布局 btn 和 lable
        layout = QGridLayout()
        layout.addWidget(textCopyButton, 0, 0)
        layout.addWidget(textLabel, 0, 1,1, 1)
        self.setLayout(layout)

        self.setWindowTitle("打水印")



    def btnClick(self):
        print('点击按钮')
        self.on_clipboard_changed()


    def on_clipboard_changed(self):
        app = QApplication(sys.argv)
        clipboard = app.clipboard() #获取剪切板
        data = clipboard.mimeData() #获取剪切板内容
        print("*" * 50)

        # 如果剪切板为文件或文件夹
        if data.hasFormat('text/uri-list'):
            urls = data.urls() #获得所有剪切文件 url
            print('剪切文件总数：%d个' % len(urls))

            for i in range(len(urls)):
                file_path = re.findall(r"'(.*)'", str(urls[i]))[0] #文件路径
                split = file_path.split('.')
                if len(split) > 1: #文件
                    file_type = split[-1]
                else: #文件夹
                    file_type = "文件夹"

                print("第%d个剪切文件类型：%s" % (i + 1, file_type))

                if file_path.startswith('file://'):
                    file_path = file_path.replace('file://', '')
                    if not os.path.exists(file_path):
                        print(print("第%d个剪切文件没有路径" % (i + 1)))
                    else:
                        print("第%d个剪切文件路径：%s" % (i + 1, file_path))
                else:
                    print("第%d个剪切文件不是以：file:// 开头")

        # 如果剪切板为文本内容
        elif data.hasText():
            print("剪切文本内容：%s" % data.text())


    def fileName(self, path):
        return os.path.basename(path)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())














#TODO: 2018年07月08日
#TODO: 1、程序点击后就异常退出问题 2、snip截图后读取的剪切板内容为空？？
#TODO: 3、我的目的是当使用截图工具后，获取剪贴板内容，如果是图片则添加水印然后将水印图片重设回剪贴板，粘贴后就是带水印的图片
#TODO：4、参考的文档在 TOBY 书签，Windows 貌似对粘贴板的监听可以很好做到，但 mac 则不行，至少目前试的方法不行























#
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
#
#
# class View(QTableView):
#     def __init__(self):
#         super(View, self).__init__(parent=None)
#
#     # def keyPressEvent(self, event):
#     #     if event.matches(QKeySequence.Copy):
#     #         print('Ctrl + C')
#     #     if event.matches(QKeySequence.Paste):
#     #         print('Ctrl + V')
#     #     QTableView.keyPressEvent(self, event)
#
#     def keyPressEvent(self, event):
#         clipboard = QApplication.clipboard()
#         if event.matches(QKeySequence.Copy):
#             print('Ctrl + C')
#             clipboard.setText("some text")
#         if event.matches(QKeySequence.Paste):
#             print(clipboard.text())
#             print('Ctrl + V')
#         QTableView.keyPressEvent(self, event)
#
# app = QApplication([])
# view = View()
# view.show()
# qApp.exec_()






# import sys
# from PyQt5.QtWidgets import QApplication
# import re
#
#
# app = QApplication(sys.argv)
# clipboard = app.clipboard() #获取剪切板
#
# def on_clipboard_changed():
#     data = clipboard.mimeData() #获取剪切板内容
#     print("*" * 50)
#
#     # 如果剪切板为文件或文件夹
#     if data.hasFormat('text/uri-list'):
#         urls = data.urls() #获得所有剪切文件 url
#         print('剪切文件总数：%d个' % len(urls))
#
#         for i in range(len(urls)):
#             file_path = re.findall(r"'(.*)'", str(urls[i]))[0] #文件路径
#             split = file_path.split('.')
#             if len(split) > 1: #文件
#                 file_type = split[-1]
#             else: #文件夹
#                 file_type = "文件夹"
#
#             print("第%d个剪切文件类型：%s" % (i + 1, file_type))
#             print("第%d个剪切文件路径：%s" % (i + 1, file_path))
#     elif data.hasText(): #如果剪切板为文本内容
#         print("剪切文本内容：%s" % data.text())
#
# #绑定信号和槽，当剪切板内容发生改变时，执行on_clipboard_changed函数
# clipboard.dataChanged.connect(on_clipboard_changed)
#
# sys.exit(app.exec_())

#普通多按钮窗口
# # !/usr/bin/env python3
# import os
# import sys
# from PyQt5.QtCore import (QMimeData, Qt)
# from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
#                              QPushButton)
# from PyQt5.QtGui import QPixmap
#
#
# class Form(QDialog):
#
#     def __init__(self, parent=None):
#         super(Form, self).__init__(parent)
#
#         textCopyButton = QPushButton("&Copy Text")
#         textPasteButton = QPushButton("Paste &Text")
#         htmlCopyButton = QPushButton("C&opy HTML")
#         htmlPasteButton = QPushButton("Paste &HTML")
#         imageCopyButton = QPushButton("Co&py Image")
#         imagePasteButton = QPushButton("Paste &Image")
#         self.textLabel = QLabel("Original text")
#         self.imageLabel = QLabel()
#         self.imageLabel.setPixmap(QPixmap(os.path.join(
#             os.path.dirname(__file__), "images/clock.png")))
#
#         layout = QGridLayout()
#         layout.addWidget(textCopyButton, 0, 0)
#         layout.addWidget(imageCopyButton, 0, 1)
#         layout.addWidget(htmlCopyButton, 0, 2)
#         layout.addWidget(textPasteButton, 1, 0)
#         layout.addWidget(imagePasteButton, 1, 1)
#         layout.addWidget(htmlPasteButton, 1, 2)
#         layout.addWidget(self.textLabel, 2, 0, 1, 2)
#         layout.addWidget(self.imageLabel, 2, 2)
#         self.setLayout(layout)
#
#         textCopyButton.clicked.connect(self.copyText)
#         textPasteButton.clicked.connect(self.pasteText)
#         htmlCopyButton.clicked.connect(self.copyHtml)
#         htmlPasteButton.clicked.connect(self.pasteHtml)
#         imageCopyButton.clicked.connect(self.copyImage)
#         imagePasteButton.clicked.connect(self.pasteImage)
#
#         self.setWindowTitle("Clipboard")
#
#     def copyText(self):
#         clipboard = QApplication.clipboard()
#         clipboard.setText("I've been clipped!")
#
#     def pasteText(self):
#         clipboard = QApplication.clipboard()
#         self.textLabel.setText(clipboard.text())
#
#     def copyImage(self):
#         clipboard = QApplication.clipboard()
#         clipboard.setPixmap(QPixmap(os.path.join(
#             os.path.dirname(__file__), "images/gvim.png")))
#
#     def pasteImage(self):
#         clipboard = QApplication.clipboard()
#         self.imageLabel.setPixmap(clipboard.pixmap())
#
#     def copyHtml(self):
#         mimeData = QMimeData()
#         mimeData.setHtml("<b>Bold and <font color=red>Red</font></b>")
#         clipboard = QApplication.clipboard()
#         clipboard.setMimeData(mimeData)
#
#     def pasteHtml(self):
#         clipboard = QApplication.clipboard()
#         mimeData = clipboard.mimeData()
#         if mimeData.hasHtml():
#             self.textLabel.setText(mimeData.html())
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     form = Form()
#     form.show()
#     app.exec_()




# 使用 main 的功能
# import main
#
# main.main()


