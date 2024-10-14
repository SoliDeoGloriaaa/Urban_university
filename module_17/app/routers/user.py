from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.future import select
from fastapi import APIRouter, Depends, status, HTTPException
from backend.db_depends import get_db
from models import User
from schemas import CreateUser, UpdateUser
from typing import Annotated

from sqlalchemy.orm import Session

router = APIRouter(prefix='/user', tags=['user'])


@router.get("/")
def all_users(db: Annotated[Session, Depends(get_db)]):
    stmt = select(User)
    users = db.execute(stmt).scalars().all()
    return users


@router.get("/user/{user_id}")
def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    stmt = select(User).where(User.id == user_id)
    user = db.execute(stmt).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user

@router.post("/create")
def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    new_user = User(**user.model_dump())
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception:
        raise HTTPException(status_code=400, detail="User already exists")
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


@router.put("/update/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    stmt = select(User).where(User.id == user_id)
    existing_user = db.execute(stmt).scalar_one_or_none()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    for key, value in user.model_dump(exclude_unset=True).items():
        setattr(existing_user, key, value)

    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}


@router.delete("/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    stmt = select(User).where(User.id == user_id)
    existing_user = db.execute(stmt).scalar_one_or_none()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    db.delete(existing_user)
    db.commit()
    return {"status_code": status.HTTP_204_NO_CONTENT}
