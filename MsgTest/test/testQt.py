from PyQt5.QtWidgets import QApplication
import sys
from PyQt5 import QtWidgets

from test.UI_testQt import Ui_Form

class myWidget(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(myWidget,self).__init__()
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myWidget()
    ex.show()
    sys.exit(app.exec_())