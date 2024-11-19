from fastapi import FastAPI
from app.models import property_model
from app.routes.property_apis import router
from app.config.config import engine

property_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/api/v1", tags=["property"])


