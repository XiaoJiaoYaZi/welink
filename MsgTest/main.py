from MainWindow import BMSMsgTest
from PyQt5.QtWidgets import QApplication
import sys



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BMSMsgTest()
    ex.show()
    sys.exit(app.exec_())
