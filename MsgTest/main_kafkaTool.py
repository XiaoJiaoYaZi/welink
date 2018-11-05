from KafkaTool import KafkaTool
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = KafkaTool()
    ex.show()
    sys.exit(app.exec_())