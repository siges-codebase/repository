from application_context import ApplicationContext
from os import environ

def load_config_on_application_context(application_context: ApplicationContext):
    application_context.config = {
        "DATABASE_URL": environ.get("DATABASE_URL")
    }