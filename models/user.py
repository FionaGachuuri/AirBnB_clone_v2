#!/usr/bin/python3
"""
This module defines a class User
which inherits from BaseModel
"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os


class User(BaseModel, Base):
    """
    Defines e user class
    """
    __tablename__ = 'users'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", passive_deletes=True, backref="user")
        reviews = relationship("Review", passive_deletes=True, backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
