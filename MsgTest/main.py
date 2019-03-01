from MainWindow import BMSMsgTest
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
import sys


#CHCP 65001

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    ex = BMSMsgTest()
    ex.show()
    sys.exit(app.exec_())
