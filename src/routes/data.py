from fastapi import FastAPI, APIRouter, Depends, UploadFile
import os
from helpers import get_settings, Settings
from controllers import DataController


# create the router
data_router = APIRouter(
    prefix="/api/v1/data",  # different prefix for data routes
    tags=["api_v1", "data"]
)

# it recives a file and uploads it to the system, using ID
@data_router.get("/upload/{project_id}")  # we need this prefix also to call the route
async def upload_data(project_id: str, file: UploadFile, app_settings: Settings = Depends(get_settings)):

    # Validate file extension (logic --> at controllers)
    is_valid = DataController().validate_file(file=file)
    
    return is_valid