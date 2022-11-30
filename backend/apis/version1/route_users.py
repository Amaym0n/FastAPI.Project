from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.repository.users import UserMethods
from db.session import get_db
from schemas.users import UserCreate, ShowUser

router = APIRouter()


@router.post(path='/users', response_model=ShowUser)
async def create_user(user: UserCreate, db: Session = Depends(dependency=get_db)):
    user = UserMethods.create_new_user(user=user, db=db)
    return user
