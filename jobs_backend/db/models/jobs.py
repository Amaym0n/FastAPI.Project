from db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean, Date


class Jobs(Base):
    """ Job table in database """

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    company_url = Column(String, nullable=True)
    location = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
