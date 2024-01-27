#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import (String, Column, ForeignKey, Integer, Float,
                        Table)
from sqlalchemy.orm import relationship

metadata = Base.metadata()

place_amenity = Table("place_amenity", metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60), ForeignKey("amenities.id"),
                             primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ Defining the class Place:
    ---------------
    A place to stay
    ---------------
    """
    __tablename__ = "places"
    city_id = Column("city_id", String(60), ForeignKey("cities.id"),
                     nullable=False)
    user_id = Column("user_id", String(60), ForeignKey("users.id"),
                     nullable=False)
    name = Column("name", String(128), nullable=False)
    description = Column("description", String(1024))
    number_rooms = Column("number_rooms", Integer, nullable=False, default=0)
    number_bathrooms = Column("number_bathrooms", Integer, nullable=False,
                              default=0)
    max_guest = Column("max_guest", Integer, nullable=False, default=0)
    price_by_night = Column("price_by_night", Integer, nullable=False,
                            default=0)
    latitude = Column("latitude", Float)
    longitude = Column("longitude", Float)
    amenity_ids = []
    cities = relationship("City", backref="place", cascade="all, delete")
    users = relationship("User", backref="place", cascade="all, delete")
    reviews = relationship("Review", backref="place",
                           cascade="all, delete")
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False,
                             back_populates="places")

    @property
    def reviews(self):
        """
        Returns a list of review instances with place_id = current place.id
        """
        from models import storage
        review_instances = []
        for key, value in storage.all().items():
            obj = key.split('.')[0]
            if obj == "reviews":
                if "place_id" in value.keys() and value["place_id"] == self.id:
                    review_instances.append(value)
        return review_instances

    @property
    def amenities(self):
        """ Returns a list of Amenity instances linked to place """
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj=None):
        """ Appends to the class attribute amenity_ids with all Amenity ids """
        if obj:
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                
