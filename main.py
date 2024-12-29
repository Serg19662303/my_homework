from fastapi import FastAPI
from app.backend.db import engine, Base
from app.routers import task, user

app = FastAPI()

@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)

Base.metadata.create_all(bind=engine)
