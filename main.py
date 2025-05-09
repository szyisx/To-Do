from fastapi import FastAPI
from routers import tasks
from database import engine
from models import Base
import uvicorn

Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0")