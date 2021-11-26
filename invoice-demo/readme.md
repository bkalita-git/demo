
this demo project based on this [postman document](https://documenter.getpostman.com/view/17779018/UVCB943R)
`Note: I considered that one transaction id can have multiple items related. so doing it as many to one relationship`

1. Clone this repo and create a python virtual env in 'demo/invoice-demo'
```
git clone github.com/bkalita-git/demo.git && cd demo/invoice-demo && python -m venv venv
```
2. Activate the environment
```
. venv/bin/activate && pip install -r requirements.txt
```
3. Setup DataBase in invoice-demo/config.py by using SQLALCHEMY_DATABASE_URI field
4. create necessary Relational Tables in the Database
```
python create_table.py
```
5. run the app
```
uvicorn main:app
```

get token
```
curl --request POST 'http://localhost:8000/token' \
-d 'username=for_demo_any_user&password=for_demo_any_password'
```

place the token in authorization header while uploading the transaction.csv file
```
curl --request POST 'http://localhost:8000/upload/' \
--header 'Accept: application/json' \
--header 'Authorization:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiZm9yX2RlbW9fYW55X3VzZXIiLCJleHAiOjE2Mzc5MTgwNDl9.v7UYuOeelpWtg_3RIiVnicHcbunmLGpcMHjfxgxwdcI' \
--form 'file=@transactions.csv'
```
other example request 
```
curl --request GET 'http://127.0.0.1:8000/generate-transactions/'
```
```
curl --request GET 'localhost:8000/purchase-list'
```
```
curl --request GET 'localhost:8000/search-transactions?awb_no=392978'
```
```
curl --request GET 'localhost:8000/search-transactions?txn_id=1001'
```
