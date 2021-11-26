from fastapi import APIRouter
from ..db import Session
import datetime 
from typing import Optional
from ..models import Transaction,PurchasedItem
from fastapi.encoders import jsonable_encoder
router = APIRouter()

@router.get('/generate-transactions/')
def gen_invoice():
	transactions = Session.query(Transaction).filter(Transaction.generated==0).all()
	invoices = []
	for transaction in transactions:
		transaction.generated=1
		invoice = transaction.as_dict()
		invoice["items"] = jsonable_encoder(transaction.items)
		
		transaction.transaction_date = datetime.date.today()
		
		invoice["transaction_date"] = transaction.transaction_date
		
		amount = 0
		for item in transaction.items:
			amount += item.price*item.qty
		
		invoice["amount"] = amount
		
		invoices.append(invoice)
		
		Session.commit()
	return invoices

@router.get('/purchase-list')
def purchase_list():
	transactions = Session.query(Transaction).filter(Transaction.generated==1).all()
	gen_transactions = []
	for transaction in transactions:
		tr = transaction.as_dict()
		tr["items"] = transaction.items
		gen_transactions.append(tr)
	return gen_transactions
		
	
@router.get('/search-transactions')
def search(awb_no: Optional[str]=None, txn_id: Optional[str]=None):
	if awb_no:
		transactions = Session.query(Transaction).filter(Transaction.AWB==awb_no).all()
		return transactions
	if txn_id:
		transactions = Session.query(Transaction).filter(Transaction.TXN_ID==txn_id).all()
		return transactions
