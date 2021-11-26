from fastapi import APIRouter, File, UploadFile, Depends, Request, HTTPException
from ..db import Session
import datetime,codecs,csv
import jwt
from config import settings
from ..models import Transaction,PurchasedItem

router = APIRouter()


def verify_jwt(request: Request):
		try:
			jwt.decode(request.headers.get('authorization'),settings.secretkey,algorithms="HS256")
		except:
			raise HTTPException(status_code=404, detail = "Invalid Token")
			
@router.post('/upload/',dependencies=[Depends(verify_jwt)])
def upload_csv(file: UploadFile = File(...)):
	data = csv.DictReader(codecs.iterdecode(file.file,'utf-8'),delimiter=',')
	for line in data:
		oid				 = line['ORDER_ID']
		item  			 = line['ITEM']
		qt   			 = line['QTY']
		pr 				 = line['PRICE']
		txn_id 			 = line['TXN_ID']
		awb 			 = line['AWB']
		tr_date 		 = line['TRANSACTION_DATE']
		gen		 		 = line['GENERATED']
		if Session.query(PurchasedItem).filter(PurchasedItem.orderid==oid).first() is None:
			try:
				row = Session.query(Transaction).filter(Transaction.TXN_ID==txn_id).one()
			except:
				row = Transaction(TXN_ID=txn_id,AWB=awb,transaction_date=tr_date,generated=gen)
			order_row = PurchasedItem(orderid=oid,name=item,qty=qt,price=pr )
			row.items.append(order_row)
			Session.add(row)
			Session.commit()
	return {"message":"successfully uploaded"}
