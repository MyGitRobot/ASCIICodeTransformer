# -*- coding: utf-8 -*-

"""
程序名称：ASCII码转换器
第一作者: MrCrawL
创建时间: 2024-01-28
最后修改: 2024-03-24
修改人: MrCrawL
Ps. 我的第一个PyQt程序，所以非常的简单！
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6.QtGui import QIcon, QPixmap
from ascii_transform_ui import Ui_Form
from mr_ico import icon_hex


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(312, 187)
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(bytes.fromhex(icon_hex))
        self.icon = QIcon(self.pixmap)
        self.setWindowIcon(self.icon)
        self.pushButton.clicked.connect(self.redirect)

        # -- 汉化 --
        self.setWindowTitle('ASCII码转换器')
        self.label.setText('字符:')
        self.label_2.setText('ASCII码:')
        self.radio.setText('字符->ASCII码')
        self.radio_2.setText('ASCII码->字符')
        self.pushButton.setText('转换')

    def Msgbox(self, msg_text:str):
        msgBox = QMessageBox()
        msgBox.setWindowIcon(self.icon)
        msgBox.setWindowTitle('提示')
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setText(msg_text)
        msgBox.addButton(QMessageBox.StandardButton.Ok)
        return msgBox

    def key_to_code(self):
        key = self.line.text()
        if len(key) == 1: self.line_2.setText(str(ord(key)))
        else: msgBox = self.Msgbox('请输入单个字符！'); msgBox.exec()

    def code_to_key(self):
        code = self.line_2.text()
        if code.isdigit():
            if 0 <= int(code) < 128: self.line.setText(chr(int(code)))
            else: msgBox = self.Msgbox('请输入0~127之间的整数！'); msgBox.exec()
        else: msgBox = self.Msgbox('请输入0~127之间的整数！'); msgBox.exec()

    def redirect(self):
        if self.radio.isChecked(): self.key_to_code()
        else: self.code_to_key()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec())
