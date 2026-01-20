# for common things used in all controllers

# e.g., app_settings
from helpers import get_settings, Settings

class BaseController:
    def __init__(self):
        self.app_settings = get_settings()