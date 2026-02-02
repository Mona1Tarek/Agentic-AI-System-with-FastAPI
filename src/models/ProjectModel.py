from .BaseDataModel import BaseDataModel
from .db_schemes import Project
from .enums.DataBaseEnums import DataBaseEnums

class ProjectModel(BaseDataModel):
    def __init__(self, db_client:object):
        super().__init__(db_client=db_client)
        # get the required data collection from the data
        self.collection = db_client[DataBaseEnums.COLLECTION_PROJECT_NAME.value]
        
    async def create_project(self, project:Project):
        result = await self.collection.insert_one(project.model_dump(by_alias=True, exclude_unset=True))     # using motor (it takes a dictionary)
        project._id = result.inserted_id
        # which means it takes a project and return the project with it's id
        return project      
    
    async def get_project_or_create_one(self, project_id: str):
        record = await self.collection.find_one({
            "project_id": project_id
        })      # this is a dict
        
        if record is None:
            project = Project(project_id=project_id)
            record = await self.create_project(project=project)
            return project
            
        return Project(**record)
    
    async def get_all_projects(self, page_number: int=1, page_size: int=10):
        total_docs = await self.collection.count_documents({})
        
        total_pages = total_docs // page_size
        if total_docs % page_size >0:
            total_pages+=1
            
        cursor = self.collection.find().skip((page_number-1)*page_size).limit(page_size)
        projects = []
        
        async for doc in cursor:
            projects.append(
                Project(**doc)
            )
            
        return projects, page_number