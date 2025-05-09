
from typing import Optional
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    completed: bool

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool

    class Config:
        orm_mode = True
