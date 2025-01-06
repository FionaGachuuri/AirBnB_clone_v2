#!/usr/bin/python3
"""
This module defines the BaseModel class for the AirBnB clone project.
It integrates SQLAlchemy for database storage and includes essential methods
for serialization, updates, and deletion.
"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models

Base = declarative_base()


class BaseModel:
    """
    Base class for all AirBnB clone models, providing common attributes
    and methods for serialization, updates, and database integration.
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """
        Instatntiates a new BaseModel model instance.
        Args:
            args (tuple): Unused.
            kwargs (dict): Key-value pairs to initialize the instance.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed
        and saves the instance to storage
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Convert instance into dict format suitable for
        JSON serialization.
        Returns:
            dict: A dictionary representation of the instance.
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        if 'created_at' in dictionary:
            dictionary['created_at'] = self.created_at.isoformat()
        if 'updated_at' in dictionary:
            dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    def delete(self):
        """
        Deletes the current instance from storage.
        """
        models.storage.delete(self)
