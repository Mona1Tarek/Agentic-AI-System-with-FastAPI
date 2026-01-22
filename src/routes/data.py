from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from helpers import get_settings, Settings
from controllers import DataController, ProjectController


# create the router
data_router = APIRouter(
    prefix="/api/v1/data",  # different prefix for data routes
    tags=["api_v1", "data"]
)

# it recives a file and uploads it to the system, using ID
@data_router.get("/upload/{project_id}")  # we need this prefix also to call the route
async def upload_data(project_id: str, file: UploadFile, app_settings: Settings = Depends(get_settings)):

    # Validate file extension (logic --> at controllers)
    is_valid, signal = DataController().validate_file(file=file)
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "Status": is_valid,
                "Signal": signal
            }
        )
    # else:
    #     return {
    #     "Status":is_valid,
    #     "Signal":signal
    # }
    
    # get the project dir path that will have the file
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    
    # get the file path itself  (why?!)
    file_path = os.path.join(
        project_dir_path,
        file.file_name
    )
    
    
    