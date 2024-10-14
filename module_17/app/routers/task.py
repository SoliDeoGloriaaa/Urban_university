from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.future import select
from backend.db_depends import get_db
from models import Task, User
from schemas import CreateTask, UpdateTask
from typing import Annotated

from sqlalchemy.orm import Session

router = APIRouter(prefix='/task', tags=['task'])


@router.get("/")
def all_tasks(db: Annotated[Session, Depends(get_db)]):
    stmt = select(Task)
    tasks = db.execute(stmt).scalars().all()
    return tasks


@router.get("/task/{task_id}")
def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    stmt = select(Task).where(Task.id == task_id)
    task = db.execute(stmt).scalar_one_or_none()
    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")
    return task


@router.post("/create")
def create_task(task: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    new_task = Task(**task.model_dump(), user_id=user_id)
    try:
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Task could not be created")
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


@router.put("/update/{task_id}")
def update_task(task_id: int, task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    stmt = select(Task).where(Task.id == task_id)
    existing_task = db.execute(stmt).scalar_one_or_none()
    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")
    for key, value in task.model_dump(exclude_unset=True).items():
        setattr(existing_task, key, value)

    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "Task update is successful!"}


@router.delete("/delete/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    stmt = select(Task).where(Task.id == task_id)
    existing_task = db.execute(stmt).scalar_one_or_none()
    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")
    db.delete(existing_task)
    db.commit()
    return {"status_code": status.HTTP_204_NO_CONTENT}
