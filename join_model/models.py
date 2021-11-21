from sqlalchemy import Column, ForeignKey, VARCHAR
from join_model.base import Base


class Restaurant(Base):
    __tablename__ = 'restaurants'
    name = Column(VARCHAR(length=255))


class Location(Base):
    __tablename__ = 'locations'
    name = Column(VARCHAR(length=255))
    memo = Column(VARCHAR(length=255))


class RestaurantDeliverableLocation(Base):
    __tablename__ = 'restaurant_deliverable_locations'
    restaurant_id = Column(ForeignKey('restaurants.id'))
    location_id = Column(ForeignKey('locations.id'))


if __name__ == '__main__':
    from database.engine import engine
    Base.metadata.create_all(engine)
