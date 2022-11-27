from PyQt5.QtWidgets import QApplication
from CustomClass import Window
from PyQt5.QtGui import QPainter, QColor
import sys
from random import randint


def randrgb():
    return randint(0, 255), randint(0, 255), randint(0, 255)


class MainWindow(Window):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.clicked = False
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Git и случайные окружности")
        self.pushButton.clicked.connect(self.draw)
        self.pushButton.setText("Добавить окружности")

    def draw(self):
        self.flag = True
        self.clicked = True
        self.update()

    def paintEvent(self, event):
        w, h = self.width(), self.height()
        if self.flag:
            self.painter = QPainter()
            self.painter.begin(self)
            for i in range(randint(10, 100)):
                color = randrgb()
                d = randint(10, 100)
                self.painter.setPen(QColor(*color))
                self.painter.setBrush(QColor(*color))
                self.painter.drawEllipse(randint(0, w), randint(0, h), d, d)
            self.painter.end()
            self.flag = False

    def resizeEvent(self, event):
        if self.clicked:
            self.flag = True


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
