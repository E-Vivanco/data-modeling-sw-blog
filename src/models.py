import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable= False)
    email = Column(String, nullable=False)
    favoritos = relationship('Favoritos', back_populates='user')

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    favoritos = relationship('Favoritos', back_populates='character')

class Planet(Base):
    __tablename__='planet'
    id= Column(Integer, primary_key=True)
    name= Column(String, nullable=False)
    favoritos= relationship('Favoritos', back_populates='planet')

class Vehicle(Base):
    __tablename__='vehicle'
    id = Column(Integer, primary_key=True)
    name= Column(String, nullable=False)
    favoritos= relationship('Favoritos', back_populates='vehicle')

class Favoritos(Base):
    __tablename__= 'favoritos'
    id = Column(Integer, primary_key=True)
    favorito_descp= Column(String, nullable=False)
    user_id= Column(Integer,ForeignKey('user.id'))
    character_id= Column(Integer,ForeignKey('character.id'))
    planet_id= Column(Integer,ForeignKey('planet.id'))
    vehicle_id= Column(Integer,ForeignKey('vehicle.id'))
    user= relationship('User', back_populates='favoritos.id')
    character= relationship('Character', back_populates='favoritos.id', uselist=False)
    planet= relationship('Planet', back_populates='favoritos.id', uselist=False)
    vehicle= relationship('Vehicle', back_populates='favoritos.id', uselist=False)
### Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
