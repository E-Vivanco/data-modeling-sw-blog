import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
#from sqlalchemy import Column, ForeignKey, Integer, Table
#from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


favoritosplanetas = Table(
    "favoritosplanetas",
    Base.metadata,
    Column("planet_id", ForeignKey("planet.id"), primary_key=True),
    Column("user_id", ForeignKey("user.id"), primary_key=True)
   )

favoritospersonajes = Table(
    "favoritospersonajes",
    Base.metadata,
    Column("character_id", ForeignKey("character.id"), primary_key=True),
    Column("user_id", ForeignKey("user.id"), primary_key=True)
    )

favoritosvehiculos = Table(
    "favoritosvehiculos",
    Base.metadata,
    Column("vehicle_id", ForeignKey("vehicle.id"), primary_key=True),
    Column("user_id", ForeignKey("user.id"), primary_key=True)
    )


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable= False)
    email = Column(String, nullable=False)
    character= relationship('Character', secondary=favoritospersonajes, uselist=True)
    planet= relationship('Planet', secondary=favoritosplanetas, uselist=True)
    vehicle= relationship('Vehicle', secondary=favoritosvehiculos, uselist=True)
    #favoritos = relationship('Favoritos', back_populates='user')

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
   # favoritospersonajes = relationship('favoritospersonajes', back_populates='character')

class Planet(Base):
    __tablename__='planet'
    id= Column(Integer, primary_key=True)
    name= Column(String, nullable=False)
  #  favoritosplanetas= relationship('favoritosplanetas', back_populates='planet')

class Vehicle(Base):
    __tablename__='vehicle'
    id = Column(Integer, primary_key=True)
    name= Column(String, nullable=False)
   # favoritosvehiculos= relationship('favoritosvehiculos', back_populates='vehicle')



#class Favoritosvehiculos(Base):
#    __tablename__='favoritosvehiculos'
#    vehicle_id= Column(Integer,ForeignKey('vehicle.id'))
#    favorito_descp= Column(String, nullable=False)
#
#class Favoritos(Base):
#    __tablename__= 'favoritos'
#    id = Column(Integer, primary_key=True)
#    favorito_descp= Column(String, nullable=False)
#    user_id= Column(Integer,ForeignKey('user.id'))
#    character_id= Column(Integer,ForeignKey('character.id'))
#    planet_id= Column(Integer,ForeignKey('planet.id'))
#    vehicle_id= Column(Integer,ForeignKey('vehicle.id'))
#    user= relationship('User', back_populates='favoritos.id')
#    character= relationship('Character', back_populates='favoritos.id', uselist=False)
#    planet= relationship('Planet', back_populates='favoritos.id', uselist=False)
#    vehicle= relationship('Vehicle', back_populates='favoritos.id', uselist=False)


### Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
