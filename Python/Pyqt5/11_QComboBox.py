import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "ali", "Three"])

        # Sends the current index (position) of the selected item.
        widget.currentIndexChanged.connect(self.index_changed)

        # There is an alternate signal to send the text.
        widget.currentTextChanged.connect(self.text_changed)

        widget.setEditable(True)

        PyQt5_flag = [QComboBox.NoInsert, QComboBox.InsertAtTop, QComboBox.InsertAtCurrent,
                      QComboBox.InsertAtBottom, QComboBox.InsertAfterCurrent,
                      QComboBox.InsertBeforeCurrent, QComboBox.InsertAlphabetically]
        widget.setInsertPolicy(QComboBox.InsertAlphabetically)
        widget.setMaxCount(5)

        self.setCentralWidget(widget)

    def index_changed(self, i):  # i is an int
        print(i)

    def text_changed(self, s):  # s is a str
        print(s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
