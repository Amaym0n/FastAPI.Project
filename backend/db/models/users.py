from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    """ User table in database """

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    jobs = relationship('Job', back_populates='owner')
