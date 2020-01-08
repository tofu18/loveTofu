import sys, random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from ui_file import Ui_Form




class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draww(qp)
        qp.end()

    def draww(self, qp):
        x, y, w = random.randrange(0, 666), random.randrange(0, 666), random.randrange(10, 300)
        qp.setBrush(QColor(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        qp.drawEllipse(x, y, w, w)

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())