from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.database import Base


class Phone(Base):
    __tablename__ = "phones"

    number = Column(String(10), primary_key=True)

    organization_phones = relationship("OrganizationPhone", back_populates="phone")
