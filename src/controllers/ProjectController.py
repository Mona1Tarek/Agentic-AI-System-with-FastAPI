from .BaseController import BaseController
from fastapi import UploadFile
import os


class ProjectController(BaseController):       
    def __init__(self):
        super().__init__()   
        
    def get_project_path(self, project_id:str):
        self.project_path = os.path.join(
            self.file_dir,
            project_id
        )
        
        if not os.path.exists(self.project_path):
            os.makedirs(self.project_path)
            
        return self.project_path
        
        