from application_context import ApplicationContext
from infrastructure.controllers.requests.product_request import ProductRequest
from infrastructure.controllers.products_controller import ProductsController
from services.dtos.product_dto import ProductDTO

def load_controllers_on_application_context(context: ApplicationContext):
    context.controllers[ProductsController] = ProductsController()

class Router():
    def __init__(self, application_context: ApplicationContext) -> None:
        self.application_context = application_context

    async def get_all_products(self):
        return self.application_context.controllers[ProductsController].get_all_products()
    
    async def insert_product(self, product: ProductRequest):
        return self.application_context.controllers[ProductsController].insert_product(product)