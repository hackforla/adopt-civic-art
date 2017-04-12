import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Piece(Base):
    __tablename__ = 'piece'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(250), nullable=False)
    latitude = Column(Integer, nullable=False)
    longitude = Column(Integer, nullable=False)
    img_url = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'img_url': self.img_url
        }

engine = create_engine('sqlite:///civicart.db')


Base.metadata.create_all(engine)
