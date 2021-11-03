from datetime import datetime

from sqlalchemy import Column, Integer, func
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import declarative_base


class Base:
    '''
    https://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/mixins.html
    '''
    id = Column(Integer, primary_key=True, autoincrement=True)
    modified_at = Column(DATETIME)
    created_at = Column(DATETIME, server_default=func.now())

    def json(self, **kwargs):
        return {}


Base = declarative_base(cls=Base)
