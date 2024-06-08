from datetime import datetime
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from flask_sqlalchemy.query import Query as BaseQuery
from sqlalchemy import inspect, Column, Integer, SmallInteger, orm
from contextlib import contextmanager


# 新定义一个类，继承导入的package（已被重命名为_SQLAlchemy)
# 链接数据库的操作函数，方便在任何时候链接数据库
class SQLAlchemy(_SQLAlchemy):
    @contextmanager  # 使得函数是上下文管理器，允许使用 with 语句来调用它
    def auto_commit(self):
        try:
            yield  # yield 将在执行 try 语句块中的部分之后，但在执行 db.session.commit() 之前暂停执行，并将控制权返回给调用者
                   # 这样做的目的是为了让调用者有机会在提交事务之前执行一些其他操作
            db.session.commit()  # 将当前事务中的所有操作（如插入、更新、删除等）永久保存到数据库中
        except Exception as e:
            db.session.rollback()  # 回滚
            raise e

db = SQLAlchemy(query_class=BaseQuery)  # BaseQuery是自定义的、在执行数据库查询时使用的默认查询类


class Base(db.Model):
    __abstract__ = True  # 抽象模型，不会创建实体表，否则需要创建主键

    # 增加一个创建时间的属性,用于记录实例对象创建的时间
    # 使用Column类来定义,列定义了一个表示时间的属性，存储整数
    #create_time = Column('create_time', Integer)

    # default=1表示未删除，=0表示已删除
    status = Column(SmallInteger, default=1)

    #def __init__(self):
        # 获取系统时间戳作为对象创建的时间
        #self.create_time = int(datetime.now().timestamp())

    # 设置对象返回字典的值(value), 同样是所有实例通用的方法，所以放在Base类中
    # 返回一些item的值，根据自己的需求
    def __getitem__(self, item):   # 参数 item表示要获取的索引或键: 'obj[key]'
        return getattr(self, item)  # 获取对象 self 中名为 item 的属性

    # 设置列属性的方法(所有实例共有)
    def set_attrs(self, attrs_dict):   # 参数 是一个字典
        for key, value in attrs_dict.items():    # 遍历字典每一条
            if hasattr(self, key) and key != 'id':   #检查 self 是否有名为 key 的属性（除了名为'id'之外）
                setattr(self, key, value)     # 设置该属性的值

    # 定义删除模型对象的方法
    def delete(self):
        self.status = 0
