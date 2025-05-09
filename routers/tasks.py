
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Task
from schemas import TaskCreate, TaskResponse, TaskUpdate
from crud import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task,
    search_task
)

router = APIRouter()

@router.post("/", response_model=TaskResponse)
def create_task_endpoint(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)

@router.get("/", response_model=List[TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return get_all_tasks(db)

@router.get("/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.patch("/{task_id}", response_model=TaskResponse)
def update_task_endpoint(task_id: int, completed: bool, db: Session = Depends(get_db)):
    task = update_task(db, task_id, completed)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}", response_model=TaskResponse)
def delete_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    task = delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get("/search", response_model=List[TaskResponse])
def search_task_endpoint(keyword: str, db: Session = Depends(get_db)):
    return search_task(db, keyword)
