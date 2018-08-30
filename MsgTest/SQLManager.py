

import pymssql


class SQKManager(object):
    def __init__(self,host,usr,pwd,db):
        self.host = host
        self.usr = usr
        self.pwd = pwd
        self.db = db
        self.cur = self.__GetConnect()

    def __GetConnect(self):
        if not self.db:
            raise (NameError,"没有设置数据库")
        self.conn = pymssql.connect(server=self.host,user=self.usr,password=self.pwd,database=self.db)
        cur = self.conn.cursor()
        if not cur:
            raise (NameError,"链接数据库失败")
        return cur

    def ExecQuery(self,sql):
        try:
            self.cur.execute(sql)
            resList = self.cur.fetchall()
            return resList
        except:
            print('error ExeQuery',sql)
            self.conn.close()


    def ExecNoQuery(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except:
            print('error ExecNoQuery')
            self.conn.rollback()
            self.conn.close()
