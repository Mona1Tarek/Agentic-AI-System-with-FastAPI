# define the schema of each collection in our database (mogo is NoSql)

from pydantic import BaseModel, Field, validator
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseModel):
    # specifications for the data formate
    _id: Optional[ObjectId]        # the key is automatically created by mongodb
    project_id: str = Field(..., min_length=1)
    
    @validator("project_id")
    def validate_project_id(cls,value):
        if not value.isalnum():
            raise ValueError('project id must be alphanumeric')
        
        return value
    
    class Config:
        arbitrary_types_allowed = True      # to raise error for ObjectId or something similar