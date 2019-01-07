import pymssql
class SQLManager(object):
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
        #cur = self.conn.cursor(as_dict=True) 返回的结果集是个dict
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
        except Exception as e:
            print(e)
            print('error ExecNoQuery')
            self.conn.rollback()
            self.conn.close()


class Field(object):
    def __init__(self,name,column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__,self.name)

class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')

class IntField(Field):
    def __init__(self,name):
        super(IntField,self).__init__(name,'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases,attrs):
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model :%s' % name)
        mapping = {}
        for k,v in attrs.items():
            if isinstance(v,Field):
                #print('Found mapping:%s ==> %s' %(k,v))
                mapping[k] = v
        for k in mapping.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mapping
        attrs['__table__'] = name
        return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError('Model object ha no attribute: %s' % item)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(self[k])
            #args.append(getattr(self,k,None))
        sql = 'insert into %s (%s) values (%s)' %(self.__table__,','.join(fields),','.join(params))
        print('SQL:%s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    id = IntField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('pwd')

import asyncio
import aiomysql

@asyncio.coroutine
def create_pool(loop,**kw):
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host','localhost'),
        port = kw.get('port',3306),
        user = kw['user'],
        password = kw['password'],
        db = kw['db'],
        chartset = kw.get('chartset','utf-8'),
        autocommit = kw.get('autocommit',True),
        maxsize = kw.get('maxsize',10),
        minsize = kw.get('minsize',1),
        loop=loop
    )
@asyncio.coroutine
def select(sql,args,size=None):
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?','%s'),args or ())
        if size:
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        return rs

@asyncio.coroutine
def execute(sql,args):
    global __pool
    with (yield from __pool) as conn:
        try:
            cur = yield from conn.cursor()
            yield from cur.execute(sql.replace('?','%s'),args or ())
            affected = cur.rowcount
            yield from cur.close()
        except BaseException as e:
            print(e)
            raise
        return affected



from DBUtils.PooledDB import PooledDB

def DBPool():
    pool = PooledDB(pymssql,5,server='10.1.120.87:1435',user='sa',password='admin123!@#',database='BMSPlatform')
    conn = pool.connection()
    cur = conn.cursor()
    cur.execute('SELECT TOP 501 t.* FROM BmsPlatform.dbo.T_Product t'.encode('utf-8'))
    resList = cur.fetchall()
    print(resList)


if __name__ == '__main__':
    # DBPool()
    # u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
    # u.save()
    db = SQLManager('10.1.120.87:1433','sa','admin123!@#','DevelopData')

    productid = 20181123
    ResourceIdList = 201811231706
    ForbiddenAreaSet    = 0
    BlacklistRank   =0

    sql = "exec ProcGetModuleListByConfigName @ConfigName = 'Web.config'"



    db.ExecQuery(sql.encode('utf-8'))

    # result = db.ExecQuery('select MobilePhoneSet from Mas_CommitMsgInfo where MsgID = 1811162127520077137'.encode('utf-8'))
    # print(len(result[0][0].split(',')))




















