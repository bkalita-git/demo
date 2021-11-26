from fastapi import APIRouter,Depends
import datetime
from fastapi.security import OAuth2PasswordRequestForm
import jwt
from config import settings
router = APIRouter()

@router.post('/token')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
	token = jwt.encode({'user':form_data.username,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=1)},settings.secretkey,algorithm="HS256")
	return {'token':token.encode('utf-8').decode('utf-8')} #will be json serialized automatically
