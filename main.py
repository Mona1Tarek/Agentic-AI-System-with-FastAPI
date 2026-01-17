from fastapi import FastAPI

# create an object of FastAPI
app = FastAPI()

# we deal with app as a decorator
@app.get("/welcome")
def welcom():
    return {
        "message": "Welcome!"
    }

# to call this function through an API 