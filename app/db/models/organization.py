from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    building_id = Column(Integer, ForeignKey("buildings.id"), nullable=False)

    building = relationship("Building", back_populates="organizations")
    phone_numbers = relationship("OrganizationPhone", back_populates="organization")
    organization_activities = relationship("OrganizationActivity", back_populates="organization")
    activities = relationship(
        "Activity",
        secondary="organization_activities",
        back_populates="organizations",
        viewonly=True,
    )

class OrganizationActivity(Base):
    __tablename__ = "organization_activities"

    organization_id = Column(Integer, ForeignKey("organizations.id"), primary_key=True)
    activity_id = Column(Integer, ForeignKey("activities.id"), primary_key=True)

    organization = relationship("Organization", back_populates="organization_activities")
    activity = relationship("Activity", back_populates="organization_associations")


class OrganizationPhone(Base):
    __tablename__ = "organization_phones"

    organization_id = Column(Integer, ForeignKey("organizations.id"), primary_key=True)
    phone_number = Column(String, ForeignKey("phones.number"), nullable=False, primary_key=True)

    organization = relationship("Organization", back_populates="phone_numbers")
    phone = relationship("Phone", back_populates="organization_phones")
