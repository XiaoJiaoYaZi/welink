from PyQt5 import QtWidgets, QtCore
from PyUI.UI_KafkaTool import Ui_KafkaTool
from configparser import ConfigParser
from pykafka import Cluster,handlers
from threading import Timer,Thread,Event
import time
from collections import namedtuple


ConsumerDescrip = namedtuple('ConsumerDescrip',
    ['Partition','LogSize','group_id','member_id','client_id','client_host']
)

ConsumerOffsets = namedtuple('Consumers',
    ['consum_group','descrips']
)

class Descrip4Consumer(object):
    def __init__(self,descrips_consumer):
        descrips = {}
        for descrip in descrips_consumer:
            pass


class ClusterManager(Thread):
    def __init__(self,host,timeInterval = 1):
        Thread.__init__(self)
        self._host = host
        self._interval = timeInterval
        self.finished = Event()
        self._handler = handlers.ThreadingHandler()
        self._cluster = Cluster(hosts=self._host,handler=self._handler)


    def cancel(self):
        self.finished.set()

    def _get_group_descrips(self):
        self._consumer_descrips = self._cluster.get_managed_group_descriptions()
        self._offsets = self._cluster.get_group_coordinator(self._consumer_descrips.keys())

    def _update(self):
        print('update')
        self._cluster.update()
        self._consumer_descrips = self._cluster.get_managed_group_descriptions()


        pass


    def run(self):
        while not self.finished.is_set():
            self._update()
            time.sleep(self._interval)
        print('run')




class KafkaTool(QtWidgets.QWidget,Ui_KafkaTool):
    sendCmd_signal = QtCore.pyqtSignal(str)
    def __init__(self,parent = None):
        super(KafkaTool,self).__init__(parent=parent)
        self.setupUi(self)



if __name__ == '__main__':
    pass