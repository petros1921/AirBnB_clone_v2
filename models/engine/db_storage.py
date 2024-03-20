#!/usr/bin/python3
""" A class with new for sqlAlchemy """

from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base


class DBStorage:
    """ create tables in environmental for athe db storage"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return a cls and self for the comand
        """
        dictinoary = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elemnt in query:
                key = "{}.{}".format(type(elemnt).__name__, elemnt.id)
                dic[key] = elemnt
        else:
            engin_list = [State, City, User, Place, Review, Amenity]
            for clase in engin_list:
                query = self.__session.query(clase)
                for elemnt in query:
                    key = "{}.{}".format(type(elemnt).__name__, elemnt.id)
                    dic[key] = elemnt
        return (dictionary)

    def new(self, obj):
        """Element will be added which is new
        """
        self.__session.add(obj)

    def save(self):
        """Changes will be save by this def
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Element in the table will be delated with this def
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """Reload the engine
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()
