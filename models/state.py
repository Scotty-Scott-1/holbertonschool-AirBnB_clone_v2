#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ The State class, contains state ID and name """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances with
            state_id equals to the current State.id for FileStorage
            """
            from models import storage
            return [city for city in storage.all().values()
                    if isinstance(city, City) and city.state_id == self.id]
