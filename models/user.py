#!/usr/bin/python3
"""This is the user class"""

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
<<<<<<< HEAD
if models.storage_t == 'db':
=======
>>>>>>> e5128cea5927c4f37e96faf3490c0939894f8182
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    reviews = relationship('Review', backref='user', cascade='delete')
    places = relationship('Place', backref='user', cascade='delete')

else:
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
