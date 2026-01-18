from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()   # it's better to make the load_dotenv() call here in main.py, so all modules can access the env variables

from routes import base

 

# create an object of FastAPI
app = FastAPI()

app.include_router(base.base_router)






