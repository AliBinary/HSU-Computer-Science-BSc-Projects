import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel,)
from PyQt5.QtCore import Qt

"""
PyQt5_flag = [Qt.AlignLeft, Qt.AlignRight, Qt.AlignHCenter,
                Qt.AlignJustify, Qt.AlignTop, Qt.AlignBottom,
                Qt.AlignVCenter, Qt.AlignCenter]
"""


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        widget.setText("Good By!")

        self.setCentralWidget(widget)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
