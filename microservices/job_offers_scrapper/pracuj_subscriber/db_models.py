from sqlalchemy import Column, String, Integer, DateTime, Date, Boolean, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base


class Responsibility(Base):
    __tablename__ = "responsibility"
    id = Column(Integer, primary_key=True, index=True)
    responsibility = Column(String(2048))
    job_offer_id = Column(Integer, ForeignKey("job_offer.id", ondelete="CASCADE"))


class Requirement(Base):
    __tablename__ = "requirement"
    id = Column(Integer, primary_key=True, index=True)
    requirement = Column(String(2048))
    must_have = Column(Boolean)
    job_offer_id = Column(Integer, ForeignKey("job_offer.id", ondelete="CASCADE"))


class Benefit(Base):
    __tablename__ = "benefit"
    id = Column(Integer, primary_key=True, index=True)
    benefit = Column(String(2048))
    job_offer_id = Column(Integer, ForeignKey("job_offer.id", ondelete="CASCADE"))


class JobOffer(Base):
    __tablename__ = "job_offer"
    id = Column(Integer, primary_key=True, index=True)
    link = Column(String(256), unique=True)
    city = Column(String(64))
    category = Column(String(64))
    title = Column(String(256))
    company_name = Column(String(256))
    earning_value_from = Column(Integer)
    earning_value_to = Column(Integer)
    contract_type = Column(String(64))
    seniority = Column(String(64))
    offer_deadline = Column(Date)
    working_mode = Column(String(64))
    working_time = Column(String(64))
    remote_recruitment = Column(Boolean)
    immediate_employment = Column(Boolean)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    responsibilities = relationship("Responsibility", backref="job_offer", cascade="all, delete-orphan")
    requirements = relationship("Requirement", backref="job_offer", cascade="all, delete-orphan")
    benefits = relationship("Benefit", backref="job_offer", cascade="all, delete-orphan")

    @staticmethod
    def get_offer_by_link(db, link):
        return db.query(JobOffer).filter(JobOffer.link == link).first()

    @staticmethod
    def get_offer_by_id(db, offer_id):
        return db.query(JobOffer).filter(JobOffer.id == offer_id).first()

    @staticmethod
    def get_empty_offers(db):
        return db.query(JobOffer).filter(JobOffer.title == None)
