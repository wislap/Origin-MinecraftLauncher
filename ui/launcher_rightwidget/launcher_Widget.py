from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QListWidget, QListWidgetItem, QFrame, \
    QGridLayout, QSlider, QScrollArea, QHBoxLayout, QVBoxLayout, QTableWidget, QHeaderView, QStackedWidget
from PySide6.QtCore import QObject, Signal, Qt
from PySide6.QtCore import Signal


class class_launcher_rightwidget:
    def main_class_launcher_rightwidget(self, parent):

        self.launcher_RightWidgetTab = QStackedWidget()

        self.classmethod_Launch_rightwidget(parent)
        self.classmethod_InstanceWidget_rightwidget(parent)
        self.classmethod_accounts_rightwidget(parent)

        self.launcher_RightWidgetTab.addWidget(self.accounts_rightwidget_frame)
        self.launcher_RightWidgetTab.addWidget(self.InstanceWidget_rightwidget_frame)
        self.launcher_RightWidgetTab.addWidget(self.Launch_rightwidget_frame)

        self.launcher_RightWidgetTab.setCurrentIndex(2)

    def classmethod_Launch_rightwidget(self, parent):
        self.parent = parent

        self.Launch_rightwidget_frame = QWidget()
        self.Launch_rightwidget_layout = QVBoxLayout()
        self.Launch_rightwidget_frame.setLayout(self.Launch_rightwidget_layout)

        self.Launch_rightwidget_Account_Picture_frame = QFrame()

        self.Launch_rightwidget_LaunchButton_button = QPushButton("启动游戏")
        #self.Launch_rightwidget_LaunchButton_button.setFixedSize(50, 50)

        self.Launch_rightwidget_InstanceButton_button = QPushButton("实例列表")
        #self.Launch_rightwidget_InstanceButton_button.setFixedSize(50, 50)

        self.Launch_rightwidget_layout.addWidget(self.Launch_rightwidget_Account_Picture_frame)
        self.Launch_rightwidget_layout.addWidget(self.Launch_rightwidget_LaunchButton_button,Qt.AlignJustify)
        self.Launch_rightwidget_layout.addWidget(self.Launch_rightwidget_InstanceButton_button,Qt.AlignJustify)
        self.Launch_rightwidget_InstanceButton_button.clicked.connect(
            self.Launch_rightwidget_InstanceButton_button_Clicked_costomsignal)

    def Launch_rightwidget_InstanceButton_button_Clicked_costomsignal(self):
        print(1)
        self.launcher_RightWidgetTab.setCurrentIndex(1)

    def classmethod_InstanceWidget_rightwidget(self, parent):

        self.InstanceWidget_rightwidget_frame = QWidget()
        self.InstanceWidget_rightwidget_layout = QVBoxLayout()
        self.InstanceWidget_rightwidget_frame.setLayout(self.InstanceWidget_rightwidget_layout)
        # self.launcher_rightwidget_frame.setFrameShape(QFrame.Box)
        # self.launcher_rightwidget_frame_layout = QHBoxLayout(self)
        self.InstanceWidget_MC_list = ["E6E", "添加新实例"]
        # self.launcher_rightwidget_frame_ScrollArea = QScrollArea()
        # self.launcher_rightwidget_frame.setStyleSheet('QWidget{background:transparent}')

        # self.rightwidget_layout.addWidget(self.launcher_rightwidget_frame_ScrollArea)
        # self.launcher_rightwidget_frame_ScrollArea.setWidget(self.launcher_rightwidget_frame)
        self.InstanceWidget_rightwidget_MCinstance_Table = QTableWidget(5, 5)
        self.InstanceWidget_rightwidget_MCinstance_Table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.InstanceWidget_rightwidget_MCinstance_Table.horizontalHeader().hide()
        self.InstanceWidget_rightwidget_MCinstance_Table.verticalHeader().hide()

        m = 0
        n = 0
        for i in self.InstanceWidget_MC_list:

            m += 1
            if i == 10:
                n += 1
                m = 1

            addFirstMCinstance_button = QPushButton(text=i)
            # addFirstMCinstance_button.setStyleSheet("QPushButton{color:blue;background-color:blue;}")
            self.InstanceWidget_rightwidget_MCinstance_Table.setCellWidget(n, m - 1, addFirstMCinstance_button)
        self.InstanceWidget_rightwidget_layout.addWidget(self.InstanceWidget_rightwidget_MCinstance_Table)

    def classmethod_accounts_rightwidget(self, parent):
        self.accounts_rightwidget_frame = QWidget()
        self.accounts_rightwidget_layout_main = QVBoxLayout()
        self.accounts_rightwidget_layout_top = QHBoxLayout()
        self.accounts_rightwidget_frame.setLayout(self.accounts_rightwidget_layout_main)

        self.accounts_rightwidget_layout_top.addStretch(0.1)

        self.accounts_AddNewAccount = QPushButton("添加新账号")
        self.accounts_rightwidget_layout_top.addWidget(self.accounts_AddNewAccount)
        self.accounts_rightwidget_layout_top.addStretch(0.1)

        self.accounts_rightwidget_layout_main.addLayout(self.accounts_rightwidget_layout_top, Qt.AlignTop)

        self.accounts_List = QTableWidget(1, 3)
        self.accounts_List.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.accounts_List.horizontalHeader().hide()
        self.accounts_List.verticalHeader().hide()

        self.accounts_rightwidget_layout_main.addWidget(self.accounts_List)
