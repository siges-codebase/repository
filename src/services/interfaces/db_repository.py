from abc import ABC, abstractmethod
from domain.product import Product
from services.dtos.product_dto import ProductDTO

class DBRepository(ABC):
    @abstractmethod
    def get_all_products() -> list[Product]:
        pass

    @abstractmethod
    def insert_product(self, product: ProductDTO) -> Product:
        pass