from infrastructure.gateways.database.postgres_repository import PostgresRepository
from services.interfaces.db_repository import DBRepository

def get_db_repository() -> DBRepository:
    return PostgresRepository()