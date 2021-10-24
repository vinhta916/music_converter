import uvicorn
from fastapi import FastAPI
from datetime import datetime


from routers.api import router as api_router # import the routes

app = FastAPI()
app.include_router(api_router, prefix="/api") # set prefix to /api



@app.get("/api/hello")
def read_root():
    date = datetime.today()
    return {"Hello": "World it is {}".format(date)}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)