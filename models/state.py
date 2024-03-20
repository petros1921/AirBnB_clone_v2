#!/usr/bin/python3
""" This is a class State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel):
    """ This is the State class with an input_name """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        var = models.storage.all()
        lista = []
        result = []
        for m in var:
            city = m.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(var[m])
        for list_elm in lista:
            if (list_elm.state_id == self.id):
                result.append(list_elm)
        return (result)
