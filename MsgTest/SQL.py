from PyUI.UI_SQL import Ui_SQL
from PyQt5 import QtWidgets
from SQLManager import SQKManager

sql_get_Modulebase = "select * from [dbo].[T_ModuleBase]".encode('utf-8')
sql_get_ConfigBase = "select * from [dbo].[T_ConfigBase]".encode('utf-8')
sql_get_MoudulesReS = "SELECT t.* FROM DevelopData.dbo.T_ModulesRelationship t".encode('utf-8')
sql_get_ConfigReS = "SELECT t.* FROM DevelopData.dbo.T_ModuleConfigRelationship t".encode('utf-8')


class Node(object):
    def __init__(self):
        self._key = 0
        self._value = []



class SQLView(QtWidgets.QDialog,Ui_SQL):
    def __init__(self,parent = None):
        super(SQLView,self).__init__(parent=parent)
        self.setupUi(self)
        self.__db = None
        self._ConfigBase = {}
        self._MouduleBase = {}
        self._tree = {}
        self._tree_config = {}
        self.initUI()
        self._connections()


    def initUI(self):
        self.treeMenu = QtWidgets.QMenu(self)
        self.treeMenu.addAction(self.action_add)
        self.treeMenu.addAction(self.action_del)
        self.pushButton_fresh.setEnabled(False)

    def _connections(self):
        self.T_ModulesRelationship.customContextMenuRequested.connect(self.showMenu)
        self.action_del.triggered.connect(self.deleteTree)
        self.action_add.triggered.connect(self.addTree)

    def deleteTree(self):
        del self.curitem
        print('del')

    def addTree(self):
        print(self.curitem)
        print('add')

    def showMenu(self,pos):
        self.curitem = self.T_ModulesRelationship.itemAt(pos)
        if self.curitem is not None:
            t = self.curitem.type()
            print(t)
        else:
            pass

        self.treeMenu.move(self.T_ModulesRelationship.cursor().pos())
        self.treeMenu.show()

    def on_connect_pressed(self):
        self.pushButton_fresh.setEnabled(True)
        self.__db = SQKManager(self.host.text(),
                               self.usr.text(),
                               self.pwd.text(),
                               self.db.text())

        #result = self.__db.ExecQuery(sql_get_ConfigBase)

    def on_pushButton_fresh_pressed(self):
        try:
            self.T_ModulesRelationship.clear()
            self._tree_config.clear()
            self._tree.clear()
            self._getdatabase()
            self._getRelationShip()
            self._maketree()
            self._maketree_config()
        except Exception as e:
            print(e)

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

        results = self.__db.ExecQuery(sql_get_ConfigReS)

        for result in results:
            key = int(result[0])
            value = int(result[1])
            if key not in self._tree_config.keys():
                self._tree_config[key] = []
            self._tree_config[key].append(value)

    def _maketree_config(self):
        try:
            for key in self._tree_config.keys():
                values = self._tree_config[key]
                item = QtWidgets.QTreeWidgetItem(self.T_ModuleConfigRelationship,[str(self._MouduleBase[key])])
                for value in values:
                    QtWidgets.QTreeWidgetItem(item,[str(self._ConfigBase[value])])
        except Exception as e:
            print(e)


    def _maketree(self):
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