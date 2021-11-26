from fastapi import FastAPI 

def create_app():
	app = FastAPI()
	from .routers import transactions,upload,login
	app.include_router(transactions.router)
	app.include_router(upload.router)
	app.include_router(login.router)
	return app
