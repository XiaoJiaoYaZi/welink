

import pymssql
import _mssql
import threading
import time
# update_ = '''DELETE FROM T_CommitInfo_WaitCheck WHERE 1=1
# #     DECLARE @id int
# #     SET @id = 2
# #     WHILE @id <100000
# #     BEGIN
# #         INSERT INTO T_CommitInfo_WaitCheck (MsgID,AccId,PrdExId,SubmitPrdExId,MobileQuantity,ChargeQuantity,MsgState,LastAuditorId,MsgType,MsgLen,[Priority],
# #         FlagBits,StartSendTime,EndSendTime,StartSendDateTime,EndSendDateTime,CommitDateTime,TotalRepFldRsndTimes,TotalSndFldRsndTimes,FailedType,SubmitType,
# #         ExtendNumber,CommitIp,AccMsgId,AccSign,Title,Operator,ModifyTime,MsgContent,MobileSet) VALUES (@id,1,1,1,1,1,2,1,2,1,1,
# #         1,CAST('00:00:00' AS time),CAST('20:00:00' AS time),CAST('1999-1-1 00:00:00' AS smalldatetime),CAST('2018-10-26 00:00:00' AS smalldatetime),CAST('2018-2-26 00:00:00' AS datetime),1,1,1,1,
# #         '123','127.0.0.1','123','234','hello','word',CAST('2018-2-2 00:00:00' AS smalldatetime),'hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,hello sql,','12345678901')
# #
# #         SET @id = @id+1
# #     END
# #     DELETE FROM T_CommitInfo WHERE 1 = 1
# # '''


class Test(object):
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
        cur = self.__GetConnect()
        try:
            cur.execute(sql)
            resList = cur.fetchall()
            return resList
        except:
            print('error ExeQuery')
            self.conn.close()


    def ExecNoQuery(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except:
            print('error ExecNoQuery')
            self.conn.rollback();
            self.conn.close()

def main():
    print('测试开始...')
    print('数据准备中')
    s = Test("10.1.120.87:1435","sa","admin123!@#","BmsPlatform")
    sql = "select count(*) from T_CommitInfo"
    reslult = s.ExecQuery(sql.encode('utf-8'))
    for i in reslult:
        print(i)

def getresult(s):
    re = 0
    while 1:

        reslult = s.ExecQuery("select count(*) from T_CommitInfo_WaitCheck".encode('utf-8'))
        print("速度：",reslult[0][0] - re,"总量：",reslult[0][0])
        re = reslult[0][0]
        time.sleep(1)

if __name__ == '__main__':
    # s = Test("10.1.120.87:1435", "sa", "admin123!@#", "BmsPlatform")
    # t = threading.Thread(target=getresult,args=(s,))
    # t.start()
    import itchat

    @itchat.msg_register(itchat.content.TEXT)
    def _(msg):
        # equals to print(msg['FromUserName'])
        print(msg.fromUserName)

    @itchat.msg_register(itchat.content.TEXT)
    def text_reply(msg):
        return msg.text


    itchat.auto_login()



    itchat.search_friends()