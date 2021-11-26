from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, scoped_session
from config import settings
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)

Session = scoped_session(sessionmaker(bind=engine))


