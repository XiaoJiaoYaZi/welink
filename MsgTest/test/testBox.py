from PyQt5 import QtWidgets,QtCore,QtGui
from box import Ui_Form


class MyWidget(QtWidgets.QWidget,Ui_Form):


    def __init__(self):
        super(MyWidget,self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.normalPoint = QtCore.QPoint()
        self.initUi()
        self.beginY = QtWidgets.QApplication.desktop().height()
        # global timeCount
        self.timeCount = 0
        self.tran = 1.0

    def initUi(self):
        self.toolButton.clicked.connect(self.myClose)
        self.label.setText('这是标题')
        self.label_2.setText('这是内容')

        self.timerShow = QtCore.QTimer(self)
        self.timerShow.timeout.connect(self.myMove)
        self.timerStay = QtCore.QTimer(self)
        self.timerStay.timeout.connect(self.myStay)
        self.timerClose = QtCore.QTimer(self)
        self.timerClose.timeout.connect(self.myClose)




    def myMove(self):

        self.beginY = self.beginY-1
        self.move(self.normalPoint.x(),self.beginY)
        if self.beginY <=self.normalPoint.y():
            self.timerShow.stop()
            self.timerStay.start(1000)

    def myStay(self):

        self.timeCount +=1
        if self.timeCount >=9:
            self.timerStay.stop()
            self.timerClose.start(200)

    def myClose(self):

        if self.isEnter:
            tran = 1.0
            self.setWindowOpacity(tran)
            return
        self.tran -=0.1
        if self.tran <0.0:
            self.timerClose.stop()
            self.close()
        else:
            self.setWindowOpacity(self.tran)

    def showAs(self):
        desk = QtWidgets.QApplication.desktop()
        deskRect = desk.availableGeometry()
        self.normalPoint.setX(deskRect.width()-self.rect().width()-1)
        self.normalPoint.setY(deskRect.height()-self.rect().height())
        self.move(self.normalPoint.x(),self.normalPoint.y()-1)
        self.show()
        self.timerShow.start(5)

    def enterEvent(self, a0: QtCore.QEvent):
        self.isEnter = True

    def leaveEvent(self, a0: QtCore.QEvent):
        self.isEnter = False


from PyQt5.QtWidgets import QApplication
import sys



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.showAs()
    sys.exit(app.exec_())