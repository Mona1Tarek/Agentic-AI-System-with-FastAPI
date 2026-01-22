# for common things used in all controllers

# e.g., app_settings
from helpers import get_settings, Settings
import os

class BaseController:
    def __init__(self):
        self.app_settings = get_settings()
        
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        
        self.file_dir = os.path.join(
            self.base_dir,
            "assets/files",
        )