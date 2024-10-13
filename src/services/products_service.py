from infrastructure.gateways.database.repository_provider import get_db_repository
from services.interfaces.db_repository import DBRepository
from services.dtos.product_dto import ProductDTO

class ProductsService():
    def __init__(self, products_repository: DBRepository = get_db_repository()) -> None:
        self.products_repository = products_repository

    def get_products(self) -> list[ProductDTO]:
        products = self.products_repository.get_all_products()
        return [ProductDTO(product.name, product.description, product.price, product.id) for product in products]
    
    def insert_product(self, product: ProductDTO) -> ProductDTO:
        product = self.products_repository.insert_product(product)
        return ProductDTO(product.name, product.description, product.price, product.id)
    

def get_products_service() -> ProductsService:
    return ProductsService()