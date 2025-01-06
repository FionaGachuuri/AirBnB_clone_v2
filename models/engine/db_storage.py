#!/usr/bin/python3
"""Database storage engine for HBNB project"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import classes
from models.user import User
import models
import os


class DBStorage:
    """Manages storage using a MYSQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize the database storage engine
        """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{db}',
            pool_pre_ping=True
        )

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query all objects of a given class
        or all objects if no class is provided
        """
        result = {}
        classes = [State, City, User, Place, Amenity, Review]
        if cls:
            cls = cls if type(cls) is not str else eval(cls)
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                result[key] = obj
        else:
            for class_ in classes:
                objs = self.__session.query(class_).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    result[key] = obj
        return result

    def new(self, obj):
        """
        Add a new object to the database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes to the database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete an object from the database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create tables and initialize a new database session
        and Create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close the current session"""
        self.__session.remove()
