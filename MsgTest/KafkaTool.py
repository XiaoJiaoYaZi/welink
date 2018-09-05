from PyQt5 import QtWidgets,QtGui
from UI_KafkaTool import Ui_KafkaTool
from sslLinux import Linux

cmds =(
    'kafka-consumer-groups.sh --bootstrap-server {}:9092 --list --new-consumer',
    'kafka-run-class.sh kafka.admin.ConsumerGroupCommand --bootstrap-server {}:9092 --describe --group {}'
)


class KafkaTool(QtWidgets.QWidget,Ui_KafkaTool):
    def __init__(self,parent = None):
        super(KafkaTool,self).__init__(parent=parent)
        self.setupUi(self)
        self.InitUI()

    def InitUI(self):
        self.pushButton_close.setEnabled(False)
        self.groupBox.setEnabled(False)

    def on_pushButton_con_pressed(self):
        self.linux = Linux(self.IP.text(),
                           int(self.port.text()),
                           self.usr.text(),
                           self.pwd.text())

        if self.linux.connect():
            self.pushButton_close.setEnabled(True)
            self.pushButton_con.setEnabled(False)
            self.groupBox.setEnabled(True)

    def on_pushButton_close_pressed(self):
        self.linux.close()
        self.linux = None
        self.pushButton_close.setEnabled(False)
        self.pushButton_con.setEnabled(True)
        self.groupBox.setEnabled(False)

    def on_pushButton_search_pressed(self):
        cmd = cmds[self.comboBox.currentIndex()].format(self.IP.text()
                                                        ,self.lineEdit_param.text())
        result,p = self.linux.send(cmd)
        self.textEdit.setText(result)

    def on_pushButton_do_pressed(self):
        cmd = self.lineEdit_cmd.text()
        result,p = self.linux.send(cmd)

        self.textEdit.setText(result)

    def closeEvent(self,event):
        if self.pushButton_close.isEnabled():
            self.pushButton_close.click()
        #self.pushButton_close.pressed()
        #event.accept()


