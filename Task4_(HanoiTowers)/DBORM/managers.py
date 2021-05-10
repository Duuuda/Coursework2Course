from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from Utils import class_property


class _BaseManager:
    __databasetype__ = 'sqlite://'
    __databasepath__ = '/database.sqlite'

    @class_property
    def __tablename__(cls) -> str:
        return f'{cls.__name__}s'

    @class_property
    def __databaseurl__(cls) -> str:
        return cls.__databasetype__ + cls.__databasepath__


class _EngineManager(_BaseManager):
    __engine = None

    @class_property
    def engine(cls):
        if cls.__engine is None:
            cls.__engine = create_engine(cls.__databaseurl__, echo=False)
        return cls.__engine


class SessionManager(_EngineManager):
    __session: Session = None

    @class_property
    def session(cls) -> Session:
        if cls.__session is None or not cls.__session.is_active:
            cls.__session = sessionmaker(bind=cls.engine)()
        return cls.__session
