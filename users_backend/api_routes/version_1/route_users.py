from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.repository.users import UserMethods
from db.session import get_db
from schemas.users import UserCreate, ShowUser

router = APIRouter()


@router.post(path='/', response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(dependency=get_db)):
    user = UserMethods.create_new_user(user=user, db=db)
    return user


@router.get(path='/', response_model=ShowUser)
def get_user_info(user_id: Optional[int] = None, db: Session = Depends(dependency=get_db)):
    return UserMethods.get_user_info(user_id=user_id, db=db)

