from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class JobBase(BaseModel):
    owner_id: int
    title: Optional[str] = None
    company_name: Optional[str] = None
    company_url: Optional[str] = None
    location: str = "Remote"
    description: Optional[str] = None


class JobCreate(JobBase):
    title: str
    company_name: str
    location: str
    description: str


class ShowJob(JobBase):
    title: str
    company_name: str
    company_url: Optional[str]
    description: str
    location: str

    class Config:
        orm_mode = True
