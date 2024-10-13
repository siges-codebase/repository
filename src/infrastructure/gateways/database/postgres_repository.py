from domain.product import Product
from infrastructure.gateways.database.db_loader import DBLoader, get_db_loader
from services.interfaces.db_repository import DBRepository
from sqlalchemy.orm import Session
from services.dtos.product_dto import ProductDTO

class PostgresRepository(DBRepository):

    def __init__(self, db_loader: DBLoader = get_db_loader()) -> None:
        self.db_loader = db_loader

    def get_db(self):
        db: Session = self.db_loader._instance.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def get_all_products(self) -> list[Product]:
        db: Session = next(self.get_db())
        products = db.query(Product).all()  
        return products
    
    def insert_product(self, product: ProductDTO) -> Product:
        db: Session = next(self.get_db())
        product = Product(name=product.name, description=product.description, price=product.price)
        db.add(product)
        db.commit()
        db.refresh(product)
        return product