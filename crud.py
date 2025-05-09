
from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate
from typing import List, Optional
from sqlalchemy import or_

def create_task(db: Session, task: TaskCreate) -> Task:
    new_task = Task(title=task.title, description=task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_all_tasks(db: Session) -> List[Task]:
    return db.query(Task).all()

def get_task_by_id(db: Session, task_id: int) -> Optional[Task]:
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task_id: int, completed: bool) -> Optional[Task]:
    task = get_task_by_id(db, task_id)
    if task:
        task.completed = completed
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int) -> Optional[Task]:
    task = get_task_by_id(db, task_id)
    if task:
        db.delete(task)
        db.commit()
    return task

def search_task(db: Session, keyword: str) -> List[Task]:
    return db.query(Task).filter(
        or_(
            Task.title.ilike(f"%{keyword}%"),
            Task.description.ilike(f"%{keyword}%")
        )
    ).all()
