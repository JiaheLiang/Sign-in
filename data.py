from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///base.db', echo=True)
Base = declarative_base()

class Log(Base):
	
	__tablename__ = "logs"
	id = Column('user_id', Integer, primary_key =True)
	name = Column(String(50))
	password = Column(String(50))
	email = Column(String(50))
	type = Column(String(50))
	
	def __init__(self, name, password, email, type):
		
		self.name = name
		self.password = password
		self.email = email
		self.type = type
		
Base.metadata.create_all(engine)
		
	
