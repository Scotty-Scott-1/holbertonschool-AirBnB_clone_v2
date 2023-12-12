#!/usr/bin/python3
"""This module defines the DBStorage class for HBNB project"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel


class DBStorage:
    """This class manages the database storage for HBNB"""
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine and links it to the MySQL database"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        from models.base_model import Base

        classes = [State, City, User, Place, Review, Amenity, BaseModel]
        result = {}

        if cls:
            if cls in classes:
                query_result = self.__session.query(cls).all()
                result = {obj.__class__.__name__ +
                          '.' + obj.id: obj for obj in query_result}
        else:
            for model_class in classes:
                query_result = self.__session.query(model_class).all()
                result.update({obj.__class__.__name__ +
                               '.' + obj.id: obj for obj in query_result})

        return result

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and create the current database session"""
        from models.state import State
        from models.city import City

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.close()
