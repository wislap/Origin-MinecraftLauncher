import sys
import os

from PySide6.QtCore import Slot, QObject
from PySide6.QtGui import QFont

envpath = r'D:\Python_program\起源启动器2.0\venv\Lib\site-packages\PySide6\plugins\platforms'
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = envpath
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QStackedWidget
from PySide6.QtGui import QIcon
from ui.left_listwidget.left_listwidget import *
from ui.launcher_rightwidget.launcher_Widget import *



from custom_window import CustomWindow


@Slot()
def say_hello():
    print("Button clicked, Hello!")


class class_MainWindow_ui(CustomWindow, class_left_listwidget, class_launcher_rightwidget):
    def __init__(self):
        super().__init__()
        # self.windowEffect = WindowEffect()
        self.setWindowIcon(QIcon("example_icon.png"))
        self.setWindowTitle("起源启动器")
        self.resize(960, 540)
        self.acrylic_color = "66ccff33"
        self.use_mica = True

        # self.setAttribute(Qt.WA_NoSystemBackground)
        # self.windowEffect.setAcrylicEffect(int(self.winId()), gradientColor="66CCFF4D")
        super().main_class_launcher_rightwidget(self.main_widget)
        super().classmethod_left_listwidget_init(self.main_widget)
        self.main_widget_layout = QHBoxLayout(self.main_widget)

        self.main_widget_layout.addWidget(self.left_listwidget_widget)

        self.RightWidgetTab = QStackedWidget()
        self.RightWidgetTab.addWidget(self.launcher_RightWidgetTab)

        self.main_widget_layout.addStretch(0.1)
        # self.main_widget_layout.addWidget(self.rightwidget_frame,Qt.AlignRight)
        self.main_widget_layout.addWidget(self.RightWidgetTab, Qt.AlignRight)

        self.RightWidgetTab.setCurrentIndex(2)
    # def mousePressEvent(self, QMouseEvent):
    #    """ 移动窗口 """
    #    self.windowEffect.moveWindow(self.winId())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow_ui = class_MainWindow_ui()
    MainWindow_ui.show()
    app.exec()
