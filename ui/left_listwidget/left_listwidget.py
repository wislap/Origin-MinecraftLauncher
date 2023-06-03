import sys
import os

from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QListWidget, QListWidgetItem, QGridLayout,QHBoxLayout
from PySide6.QtCore import QObject, Signal, Qt
from ui.launcher_rightwidget.launcher_Widget import *


class class_left_listwidget(QObject):

    def classmethod_left_listwidget_init(self, parent):
        self.left_listwidget_widget = QWidget()
        self.left_listwidget_widget_layout = QVBoxLayout()
        self.left_listwidget_widget.setLayout(self.left_listwidget_widget_layout)
        self.FengdianAccount_frame = QFrame()
        self.left_listwidget_list = [ "启动游戏", "下载", "多人联机", "服务器", "设置"]

        self.left_listwidget = QListWidget(parent)
        for i in self.left_listwidget_list:
            left_listwidget_item_cache = QListWidgetItem(i)

            self.left_listwidget.addItem(left_listwidget_item_cache)

        self.left_listwidget.itemClicked.connect(self.slot_left_listwidget_item_leftclicked)

        self.left_listwidget_widget_layout.addWidget(self.FengdianAccount_frame)
        self.left_listwidget_widget_layout.addWidget(self.left_listwidget)

    def slot_left_listwidget_item_leftclicked(self, itemname):
        print(itemname.text())
