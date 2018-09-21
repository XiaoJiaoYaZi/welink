from PyQt5 import QtWidgets, QtCore
from PyUI.UI_KafkaTool import Ui_KafkaTool
from sslLinux import Linux
from configparser import ConfigParser


cmds =(
    'kafka-consumer-groups.sh --bootstrap-server {}:9092 --list --new-consumer',
    'kafka-run-class.sh kafka.admin.ConsumerGroupCommand --bootstrap-server {}:9092 --describe --group {}'
)


class KafkaTool(QtWidgets.QWidget,Ui_KafkaTool):
    sendCmd_signal = QtCore.pyqtSignal(str)
    def __init__(self,parent = None):
        super(KafkaTool,self).__init__(parent=parent)
        self.setupUi(self)
        self.init()
        self.InitUI()


    def init(self):
        self._config = ConfigParser()
        try:
            self._config.read("./config/kafkaTool.ini",encoding='gbk')
        except Exception as e:
            print(e)

    def InitUI(self):
        self.pushButton_close.setEnabled(False)
        self.groupBox.setEnabled(False)
        self.sendCmd_signal.connect(self.slot_sendCmd,QtCore.Qt.QueuedConnection)
        self.textEdit.setReadOnly(True)
        self.IP.setText(self._config['host']['ip'])
        self.pwd.setText(self._config['host']['pwd'])
        self.usr.setText(self._config['host']['usr'])
        self.port.setText(self._config['host']['port'])

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
        # result,p = self.linux.send(cmd)
        # self.textEdit.setText(result)
        self.sendCmd_signal.emit(cmd)
        print("ok")

    def slot_sendCmd(self,text):
        import time
        time.sleep(2)
        result, p = self.linux.send(text)
        self.textEdit.setText(result)



    def on_pushButton_do_pressed(self):
        cmd = self.lineEdit_cmd.text()
        result,p = self.linux.send(cmd)

        self.textEdit.setText(result)

    def saveConfig(self):
        self._config['host']['ip'] = self.IP.text()
        self._config['host']['pwd'] = self.pwd.text()
        self._config['host']['usr'] = self.usr.text()
        self._config['host']['port'] = self.port.text()
        with open("./config/kafkaTool.ini",'w',encoding='gbk') as f:
            self._config.write(f)

    def closeEvent(self,event):
        self.saveConfig()
        if self.pushButton_close.isEnabled():
            self.pushButton_close.click()
        #self.pushButton_close.pressed()
        #event.accept()


