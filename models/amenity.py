#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from base_model import Base


class Amenity(BaseModel, Base):
    name = ""
