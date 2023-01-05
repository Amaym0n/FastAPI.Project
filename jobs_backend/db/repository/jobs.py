from sqlalchemy.orm import Session

from db.models.jobs import Jobs
from schemas.jobs import JobCreate


class JobMethods:
    """ Class with methods to update/delete/create jobs """

    @staticmethod
    def create_new_job(owner_id: int, job: JobCreate, db: Session):
        job = Jobs(owner_id=owner_id, **job.dict())
        db.add(instance=job)
        db.commit()
        db.refresh(instance=job)
        return job

    @staticmethod
    def read_job(job_id: int, db: Session):
        return db.query(Jobs).get(ident=job_id)
