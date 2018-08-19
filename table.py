from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()

class User(Base):
	""""""
	__tablename__ = "users"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	gender = Column(String)
	age = Column(Integer)
	address = Column(String)
	
	def __init__(self, name, gender, age, address):
		""""""
		self.name = name
		self.gender = gender
		self.age = age
		self.address = address

Base.metadata.create_all(engine)