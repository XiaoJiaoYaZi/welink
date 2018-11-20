

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
    bar = 'bip'

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
    def __init__(self):
        super().__init__()
    def __str__(self):
        return 'F'

f = F()
