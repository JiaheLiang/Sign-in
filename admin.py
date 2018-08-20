import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data import *

engine = create_engine('sqlite:///base.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

log = Log("admin","admin","554288973@qq.com","administrator")
session.add(log)

log = Log("hacker","hacker","554288973@qq.com","administrator")
session.add(log)

session.commit()