import sys, random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())