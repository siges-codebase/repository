from application_context import ApplicationContext

def load_config_on_application_context(application_context: ApplicationContext):
    application_context.config = {
        "DATABASE_URL": "postgresql://postgres:mysecretpassword@db:5432/mydatabase"
    }