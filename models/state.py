#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os
class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128))
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            all_objs_list = []
            all_objs = storage.all(City)

            for key in all_objs.keys():

                id_obj = key.split('.')

                if id_obj[1] == self.id:
                    all_objs_list.append(all_objs[key])
            return all_objs_list
