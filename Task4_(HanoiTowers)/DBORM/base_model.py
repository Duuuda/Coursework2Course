from DBORM.managers import SessionManager
from DBORM.decorators import check_database, check_table


class BaseModel(SessionManager):
    def __init__(self, *args, **kwargs):
        need_args_count = len(self.metadata.tables[self.__tablename__].columns)
        current_args_count = len(args) + len(kwargs)
        if need_args_count != current_args_count:
            raise TypeError(f'__init__() accepts {need_args_count} arguments - submitted {current_args_count}')
        args = list(args)
        for column in self.metadata.tables[self.__tablename__].columns:
            if column.name in kwargs:
                setattr(self, column.name, kwargs[column.name])
            else:
                setattr(self, column.name, args.pop(0))

    class DoesNotExist(Exception):
        pass

    @classmethod
    @check_database
    @check_table
    def get(cls, **kwargs):
        obj = cls.session.get(cls, kwargs)
        if obj is None:
            raise cls.DoesNotExist('The object with these primary keys does not exist')
        return obj

    @classmethod
    @check_database
    @check_table
    def create(cls, *args, **kwargs):
        cls.session.add(cls(*args, **kwargs))
        cls.session.commit()

    @check_database
    @check_table
    def delete(self):
        self.session.delete(self)
        self.session.commit()

    @check_database
    @check_table
    def save(self):
        self.session.commit()
