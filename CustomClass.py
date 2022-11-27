from PyQt5.QtWidgets import QWidget, QPushButton, QStatusBar, QMainWindow
from PyQt5.QtWidgets import QSpacerItem, QSizePolicy, QVBoxLayout, QHBoxLayout


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setMinimumSize(200, 150)
        self.centralwidget = QWidget(self)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout = QVBoxLayout()
        self.horizontalLayout = QHBoxLayout()
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(200, 40)
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
