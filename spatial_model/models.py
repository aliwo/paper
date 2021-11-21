from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import VARCHAR
from spatial_model.base import Base
from geoalchemy2 import Geometry

class Restaurant(Base):
    __tablename__ = 'restaurants'
    name = Column(VARCHAR(length=255))
    deliverable_location = Column(Geometry('POLYGON', srid=4326))


if __name__ == '__main__':
    from database.engine import engine
    Base.metadata.create_all(engine)
