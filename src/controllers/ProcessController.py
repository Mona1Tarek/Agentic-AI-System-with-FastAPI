from .BaseController import BaseController
from .ProjectController import ProjectController
import os
from langchain_community.document_loaders import TextLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from models import ProcessingEnum

class ProcessController(BaseController):       
    def __init__(self, project_id: str):
        super().__init__()      
        self.project_id = project_id
        self.project_path = ProjectController().get_project_path(project_id=project_id)
        
    def get_file_extension(self, file_id: str):
        return os.path.splitext(file_id)[-1]
    
    # we need a loader to deals with all types of files
    def get_file_loader(self, file_id: str):
        file_extension = self.get_file_extension(file_id=file_id)
        file_path = os.path.join(
            self.project_path,
            file_id
        )
        
        if file_extension == ProcessingEnum.TXT.value:
            return TextLoader(file_path, encoding="utf-8")
        
        if file_extension == ProcessingEnum.PDF.value:
            return PyMuPDFLoader(file_path)
        
        return None 
    
    def get_file_content(self,file_id: str):
        loader = self. get_file_loader(file_id= file_id)    
        # bec it's a method of this class so needs self, and loader is a local variable Exists only inside this function
        
        return loader.load()    # this return a list of object of the type document(page_content, metadata)
         
    
    def process_file_content(self, file_content: list, file_id: str, 
                             chunk_size: int=100, overlap_size: int=20):
        
        # define object from the text splitter
        # this takes text
        text_content = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, 
            chunk_overlap=overlap_size,
            length_function=len
        )
        
        # extract the text and metadata from the loader
        file_content_texts = [
            rec.page_content
            for rec in file_content
        ]
        
        file_content_metadata = [
            rec.metadata
            for rec in file_content
        ]
        
        chunks = text_content.create_documents(
            file_content_texts,
            metadatas=file_content_metadata
        )
        
        return chunks
        