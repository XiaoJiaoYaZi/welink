from  UI_SQL import Ui_Form
from PyQt5 import QtWidgets,QtGui
from SQLManager import SQKManager

sql_get_Modulebase = "select * from [dbo].[T_ModuleBase]".encode('utf-8')
sql_get_ConfigBase = "select * from [dbo].[T_ConfigBase]".encode('utf-8')
sql_get_MoudulesReS = "SELECT t.* FROM DevelopData.dbo.T_ModulesRelationship t".encode('utf-8')
sql_get_ConfigReS = "select * from [dbo].[T_MoudulesConfigRelationship]".encode('utf-8')


class Node(object):
    def __init__(self):
        self._key = 0
        self._value = []



class SQLView(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(SQLView,self).__init__()
        self.setupUi(self)
        self.__db = None
        self._ConfigBase = {}
        self._MouduleBase = {}
        self._tree = {}


    def on_connect_pressed(self):
        self.__db = SQKManager(self.host.text(),
                               self.usr.text(),
                               self.pwd.text(),
                               self.db.text())

        #result = self.__db.ExecQuery(sql_get_ConfigBase)
        self._getdatabase()
        self._getRelationShip()
        self._maketree()

    def _getdatabase(self):
        results = self.__db.ExecQuery(sql_get_ConfigBase)
        if results is None:
            print('获取 ConfigBase数据失败')
            return
        for result in results:
            self._ConfigBase[result[0]] = result[1]

        results = self.__db.ExecQuery(sql_get_Modulebase)
        if results is None:
            print('获取 Modulebase数据失败')
            return
        for result in results:
            self._MouduleBase[result[0]] = result[2]

    def _getRelationShip(self):
        results = self.__db.ExecQuery(sql_get_MoudulesReS)
        #{1:{1:[8,13,23,40]},6:{6:13,23,40,42},...}
        for result in results:
            key = int(result[0])
            value = int(result[1])
            if key not in self._tree.keys():
                self._tree[key] = {key:[]}
            self._tree[key][key].append(value)


    def _maketree(self):
        trees = {}
        for key in self._tree.keys():
            #self.T_ModulesRelationship.addTopLevelItem(QtWidgets.QTreeWidgetItem(str(key)))
            self.makes(self.T_ModulesRelationship,key)

    def makes(self,item,value):
        if value not in self._tree.keys():
            QtWidgets.QTreeWidgetItem(item,[str(self._MouduleBase[value])])
            return
        it = QtWidgets.QTreeWidgetItem(item,[str(self._MouduleBase[value])])
        for var in self._tree[value][value]:
            self.makes(it,var)