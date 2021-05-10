from sqlalchemy_utils import database_exists, create_database


def check_database(func):
    def wrapper(cls, *args, **kwargs):
        if not database_exists(cls.__databaseurl__):
            create_database(cls.__databaseurl__)
        return func(cls, *args, **kwargs)
    return wrapper


def check_table(func):
    def wrapper(cls, *args, **kwargs):
        cls.metadata.create_all(cls.engine)
        return func(cls, *args, **kwargs)
    return wrapper
