from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.sql import func

from database import Base


class Estate(Base):
    __tablename__ = "estate"
    estate_id = Column(Integer, primary_key=True, index=True)
    link = Column(String(256))
    for_sale = Column(Boolean)
    estate = Column(String(128))
    city = Column(String(32))
    id_scrap = Column(Integer, unique=True)
    title = Column(String(128))
    area = Column(Integer)
    number_of_rooms = Column(Integer)
    flat_floor = Column(String(16))
    extras = Column(String(256))
    type_of_building = Column(String(64))
    bills_monthly = Column(String(16))
    market = Column(String(32))
    number_of_floors = Column(Integer)
    price_per_m2 = Column(Integer)
    price = Column(Integer)
    rent_price = Column(Integer)
    picture1 = Column(String(256))
    picture2 = Column(String(256))
    picture3 = Column(String(256))
    picture4 = Column(String(256))
    picture5 = Column(String(256))
    picture6 = Column(String(256))
    picture7 = Column(String(256))
    picture8 = Column(String(256))
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    @staticmethod
    def get_estate_by_link(db, link):
        return db.query(Estate).filter(Estate.link == link).first()

    @staticmethod
    def get_estate_by_scrap_id(db, id_scrap):
        return db.query(Estate).filter(Estate.id_scrap == id_scrap).first()

    @staticmethod
    def get_empty_estates(db):
        return db.query(Estate).filter(Estate.title == None)

    @staticmethod
    def get_all_estates(db):
        return db.query(Estate).all()
