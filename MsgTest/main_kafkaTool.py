from KafkaTool import KafkaTool
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    ex = KafkaTool()
    ex.show()
    sys.exit(app.exec_())