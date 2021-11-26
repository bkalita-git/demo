from pydantic import BaseSettings
class Settings(BaseSettings):
	app_name: str = "Invoice Generator"
	admin_email: str = "bkalita.mail@gmail.com"
	secretkey: str = "bfhrgf7bcehb387bfu43g"
	SQLALCHEMY_DATABASE_URI = 'postgresql://flask_test:password@localhost/TESTSB'

settings = Settings()
