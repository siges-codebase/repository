from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infrastructure.controllers.requests.product_request import ProductRequest
from infrastructure.controllers.router import Router, load_controllers_on_application_context
from infrastructure.gateways.database.db_loader import init_db_loader
from application_context import ApplicationContext
from utils.config_loader import load_config_on_application_context

application_context = ApplicationContext()

load_config_on_application_context(application_context)

init_db_loader(application_context)

load_controllers_on_application_context(application_context)

router = Router(application_context)

app = FastAPI()

origins = [
    "http://192.168.0.0/16",  # Permite cualquier IP dentro del rango 192.168.x.x
    "http://localhost:3000",        # Permite localhost
    "http://127.0.0.1",        # Permite localhost con 127.0.0.1
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products")
async def get_all_products():
    return await router.get_all_products()

@app.post("/products")
async def insert_product(product: ProductRequest):
    return await router.insert_product(product)