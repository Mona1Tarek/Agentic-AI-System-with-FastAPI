from .BaseController import BaseController
from fastapi import UploadFile

class DataController(BaseController):       # to inherit from BaseController (as the son)
    def __init__(self):
        super().__init__()      # calling the BaseController
        self.size_scale = 1048576
        
    def validate_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False
        
        if file.size > self.app_settings.FILE_MAX_SIZE_MB * self.size_scale:
            return False
        
        return True