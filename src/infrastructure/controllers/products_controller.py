from infrastructure.controllers.requests.product_request import ProductRequest
from services.products_service import ProductsService, get_products_service
from services.dtos.product_dto import ProductDTO

class ProductsController():
    def __init__(self, products_service: ProductsService = get_products_service()) -> None:
        print(products_service)
        self.products_service = products_service

    def get_all_products(self) -> list[ProductDTO]:
        return self.products_service.get_products()
    
    def insert_product(self, product: ProductRequest) -> ProductDTO:
        productDTO = ProductDTO(product.name, product.description, product.price)
        return self.products_service.insert_product(productDTO)




