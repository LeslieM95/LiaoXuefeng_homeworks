#!/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#定义Field类，保存数据库表的字段名和字段类型
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    #def __str__(self):
     #   return '<%s:%s>' % (self.__class__.__name__, self.name)

#定义各种类型的Field
class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, value):
        super(IntegerField, self).__init__(value, 'bigint')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        else:
            print('Found modle: %s' % name)
            mappings = {}
            for k, v in attrs.items():#k, v是类的属性, 如: ID = IntegerField('ids')
                if isinstance(v, Field):#k == ID, v == IntegerField('ids')
                    print('Found mapping: %s ==> %s' % (k, v))#print(v)会调用Field的__str__()方法
                    mappings[k] = v
            for k in mappings.keys():
                attrs.pop(k)
            attrs['__mappings__'] = mappings
            attrs['__table__'] = name
            return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass = ModelMetaclass):

    def __init__(self, *args):  # 若没有**kw和*args, 则只能用u['name']='Michael' 的形式传入  
        super(Model, self).__init__(*args)  # __init__中有**kw时, 才能用u=User(name='Michael', ...)作为关键字参数传入
                                           # __init__中有*args时, 才能用u=User([('name', 'Michael'), ...])作为位置参数传入

    def __getattr__(self, key):#key并不是Model实例的属性, 通过__getattr__可以把key设置为attribute
        try:
            return self[key]#把key对应的value当做attribute的值返回, 使之可以通过属性来访问
        except KeyError:#u.key, 当key不存在时, 报错
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):#'u.score = 98' 会调用__setattr__, 可以把score设置为attribute, 同时成为字典u的一个key
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(k)
            print(k, v, v.name)
            params.append('?')
            args.append(getattr(self, k, 404))  # 若k不存在, 则返回404
        sql='insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    ID = IntegerField('ids')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# __init__中有*args(其实是positional argument)时的传入方式
u = User([('id', 12345), ('name', 'michael'), ('email', 'test@orm.org'), ('password', '19950110')]) 

# __init__中有**kw时的传入方式
#u = User(id=12345, name='Michael', email='test@orm.org', password='my-password')

#__init__()中什么都没有, 只能一个个传入
#u = User()
#u['ID'] = 12345
#u['name'] = 'Michael'
#u['email'] = 'test@orm.org'
#u['password'] = 'my-password'
u.save()
