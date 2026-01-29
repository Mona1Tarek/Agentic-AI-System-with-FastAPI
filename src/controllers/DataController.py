from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
import re
from .ProjectController import ProjectController
import os

class DataController(BaseController):       # to inherit from BaseController (as the son)
    def __init__(self):
        super().__init__()      # calling the BaseController
        self.size_scale = 1048576
        
    def validate_file(self, file: UploadFile):        
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        
        if file.size > self.app_settings.FILE_MAX_SIZE_MB * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value
        
        return True, ResponseSignal.FILE_VALIDATED_SUCCESSFULLY.value
    
    
    def get_clean_file_name(self, orig_file_name: str):
        # remove any special characters, except underscore and .
        cleaned_file_name = re.sub(r'[^\w.]', '', orig_file_name.strip())

        # replace spaces with underscore
        cleaned_file_name = cleaned_file_name.replace(" ", "_")

        return cleaned_file_name
    
    
    def get_unique_file_path(self, orig_file_name: str, project_id: str):
        clean_file_name = self.get_clean_file_name(orig_file_name=orig_file_name)
        random_key = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)
        
        new_file_path = os.path.join(
            project_path,
            random_key + "_" + clean_file_name
        )
        
        # if the file exists, generate a new random key and try again
        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(
                project_path,
                random_key + "_" + clean_file_name
            )
            
        return new_file_path, random_key + "_" + clean_file_name
        
    
