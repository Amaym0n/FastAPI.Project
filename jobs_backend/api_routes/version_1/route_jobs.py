from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.repository.jobs import JobMethods
from db.session import get_db
from schemas.jobs import JobCreate, ShowJob

router = APIRouter()


@router.post(path='/{owner_id}', response_model=ShowJob)
def create_job(owner_id: int, job: JobCreate, db: Session = Depends(dependency=get_db)):
    job = JobMethods.create_new_job(owner_id=owner_id, job=job, db=db)
    return job


@router.get(path='/{owner_id}', response_model=ShowJob)
def read_job(owner_id: int, job_id: Optional[int] = None, db: Session = Depends(dependency=get_db)):
    job = JobMethods.read_job(job_id=job_id, db=db)
    return job
