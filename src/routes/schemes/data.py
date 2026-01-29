from pydantic import BaseModel, Field
from typing import Optional

class ProcessRequest(BaseModel):        # this is the request body schema for the processing endpoint
    file_id: str = Field(..., description="The unique identifier of the file to be processed.")
    chunk_size: Optional[int] = 100
    overlap_size: Optional[int] = 20
    do_reset: Optional[int] = 0     # do --> bec it's a user parameter action
    