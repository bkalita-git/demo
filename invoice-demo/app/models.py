from .db import engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import ForeignKey, Column, Integer, String, Float, Date

import datetime

Base  = declarative_base()

class Transaction(Base):
	__tablename__ = 'transactions'
	
	TXN_ID = Column(Integer, primary_key=True, nullable=False)
	AWB = Column(Integer)
	transaction_date = Column(Date, default=datetime.date.today)
	generated = Column(Integer, default=0)
	
	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}
class PurchasedItem(Base):
	__tablename__ = 'purchaseditems'
	
	orderid = Column(Integer, primary_key=True, nullable=False)
	name = Column(String)
	qty = Column(Integer,default=1)
	price = Column(Float,nullable=False)
	tid = Column(Integer, ForeignKey('transactions.TXN_ID'))
	transaction=relationship("Transaction",backref="items")
	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}
