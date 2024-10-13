from application_context import ApplicationContext
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

def init_db_loader(context: ApplicationContext):
    DBLoader._instance = DBLoader(context)
    Base.metadata.create_all(DBLoader._instance.engine)

class DBLoader:
    _instance = None
    _initialized = False
    SessionLocal = None
    Base = None
    engine = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DBLoader, cls).__new__(cls)
        return cls._instance

    def __init__(self, context: ApplicationContext):
        if not self._initialized:

            DATABASE_URL = context.config["DATABASE_URL"]

            self.engine = create_engine(DATABASE_URL)

            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

            self.initialized = True

def get_db_loader() -> DBLoader:
    return DBLoader.__new__(DBLoader)
