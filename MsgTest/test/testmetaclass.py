




def upper_attr(future_class_name,future_class_parent,future_class_attr):
    attrs = ((name,value) for name,value in future_class_attr.items() if not name.startswith('__'))
    uppercase_attr = dict((name.upper(),value) for name,value in attrs)
    #通过type创建类对象
    return type(future_class_name,future_class_parent,uppercase_attr)

#metaclass = upper_attr

#Foo中有__metaclass__这个属性吗？如果是，Python会在内存中通过
# __metaclass__创建一个名字为Foo的类对象（我说的是类对象，请紧跟我的思路）。
# 如果Python没有找到__metaclass__，它会继续在Bar（父类）中寻找__metaclass__属性，
# 并尝试做和前面同样的操作。如果Python在任何父类中都找不到__metaclass__，
# 它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。
# 如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。

class Foo(object,metaclass=upper_attr):
    a = '1'

print(hasattr(Foo,'bar'))
print(hasattr(Foo,'BAR'))


class UpperAttrMetaClass(type):
    def __new__(upperattr_metaclass,future_class_name,future_class_parent,future_class_attr):
        attrs = ((name,value) for name,value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(),value) for name,value in attrs)
        return type.__new__(upperattr_metaclass,future_class_name,future_class_parent,uppercase_attr)


class MetaClass(type):
    def __new__(cls, name,base,dct):
        #name为类的名字
        #base为基类
        #dct为类的属性
        print(dct)
        attrs = ((name,value) for name,value in dct.items() if not name.startswith('__'))
        upper_attr = dict((name.upper(),value) for name,value in attrs)
        return super(MetaClass,cls).__new__(cls,name,base,upper_attr)

class F(dict,metaclass=MetaClass):
    f = 'f'
    # def __init__(self):
    #     super().__init__()
    def __str__(self):
        return 'F'

f = F()

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print('singleton',s1 is s2)

class MetaSingleton(type):
    def __init__(self,*args,**kwargs):
        self._instance = None
        super(MetaSingleton,self).__init__(*args,**kwargs)

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super(MetaSingleton,self).__call__(*args,*kwargs)
        return self._instance

class Singleton1(object,metaclass=MetaSingleton):
    pass

s1 = Singleton1()
s2 = Singleton1()
print('singleton1',s1 is s2)

class test(object):
    def __init__(self):
        print('init')
    def __call__(self, *args, **kwargs):
        print('call')
    def __new__(cls, *args, **kwargs):
        print('new')
        return super(test,cls).__new__(cls,*args,**kwargs)

t = test()
t()


import abc
class Base(object,metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def func_a(self,data):
        '''
        :param data:
        :return:
        '''
    @abc.abstractmethod
    def func_b(self,data,out):
        print('func_b in Base')
        '''
        :param data:
        :param out:
        :return:
        '''
    def func_d(self):
        print('func_d in base')

class Register(object):
    def func_c(self):
        print('func_c in third class')

    def func_a(self,data):
        print('func_a in third class',data)

class Sub(Base):

    def func_a(self,data):
        print('over write func_a',data)

    def func_b(self,data,out):
        super(Sub,self).func_b(data,out)
        print('over write func_b')

    def func_d(self):
        super(Sub,self).func_d()
        print('func_d in sub')

    # def func_c(self):
    #     print('Sub:func_c')
print(issubclass(Register,Base))
#注册虚子类
Base.register(Register)
r = Register()
r.func_c()
r.func_a(123)
print(issubclass(Register,Base))

print(issubclass(Sub,Base))


s = Sub()
s.func_a('123')
s.func_b(123,123)
s.func_d()

