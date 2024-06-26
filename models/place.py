#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from os import getenv
# from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column("city_id", String(
        60), ForeignKey("cities.id"), nullable=False)
    user_id = Column("user_id", String(
        60), ForeignKey("users.id"), nullable=False)
    name = Column("name", String(128), nullable=False)
    description = Column("description", String(1024), nullable=True)
    number_rooms = Column("number_rooms", Integer, nullable=False, default=0)
    number_bathrooms = Column("number_bathrooms", Integer,
                              nullable=False, default=0)
    max_guest = Column("max_guest", Integer, nullable=False, default=0)
    price_by_night = Column("price_by_night", Integer,
                            nullable=False, default=0)
    latitude = Column("latitude", Float, nullable=True)
    longitude = Column("longitude", Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="state",
                               cascade="all,delete-orphan")
        # id = Column(String(60), primary_key=True, nullable=False)
    else:
        def reviews(self):
            from models.review import Review
            import models
            temp = {}
            for k, v in models.storage.all(Review).items():
                if v.to_dict()["Place.id"] == self.id:
                    temp.update({k, v})
            return temp

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
