__author__ = 'Anuj'

from PyQt4 import QtCore,QtGui
from ui_calculator import Ui_calculator


class calculator( QtGui.QMainWindow, Ui_calculator):
    def __init__(self):
        super(calculator, self).__init__()
        self.setupUi(self)
        self.oneButton.clicked.connect(self.display_1)

    def display_1(self):
        print "Onebutton clicked"
        self.lineEdit.setText("1")


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = calculator()
    ui.show()
    sys.exit(app.exec_())
