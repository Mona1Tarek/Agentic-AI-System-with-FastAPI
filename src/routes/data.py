from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from helpers import get_settings, Settings
from controllers import DataController, ProjectController
import aiofiles as aiof
from models import ResponseSignal
import logging

logger = logging.getLogger("uvicorn.error")

# create the router
data_router = APIRouter(
    prefix="/api/v1/data",  # different prefix for data routes
    tags=["api_v1", "data"]
)


# it recives a file and uploads it to the system, using ID
@data_router.post("/upload/{project_id}")  # we need this prefix also to call the route
async def upload_data(project_id: str, file: UploadFile, app_settings: Settings = Depends(get_settings)):

    data_controller_obj = DataController()

    # Validate file extension (logic --> at controllers)
    is_valid, signal = data_controller_obj.validate_file(file=file)
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "Signal": signal
            }
        )
   
    # get the file path itself  
    # it's better to make the file name unique 
    file_path = data_controller_obj.get_unique_file_path(
        orig_file_name=file.filename,
        project_id=project_id
    )
    
    # open the file path and write the file in binary 
    # reads an uploaded file in small chunks and writes it asynchronously to disk
    try:        # to handle any unexpected error during file operations
        async with aiof.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error uploading file: {e}")
        
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "Signal": ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )
   
                
    return JSONResponse(
            content={
                "Signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value
            }
        )
    