from fastapi import FastAPI, APIRouter
import os


# create an object of APIRouter
base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)

# we deal with base_router as a decorator
@base_router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    
    return {
        "APP_NAME": app_name,
        "APP_VERSION": app_version
    }
