from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from settings import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session() -> Session:
    session = SessionFactory()
    try:
        yield session
    finally:
        session.close()
