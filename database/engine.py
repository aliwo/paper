# import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

MYSQL = 'mysql+pymysql://root:22380476@127.0.0.1/paper?charset=UTF8MB4'
POSTGRESQL = 'postgresql+psycopg2://postgres:22380476@127.0.0.1:7432/paper'

engine = create_engine(POSTGRESQL, pool_recycle=300, )
SessionMaker = sessionmaker(bind=engine)

