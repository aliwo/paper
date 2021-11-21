import time
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event


logging.basicConfig()
logger = logging.getLogger("myapp.sqltime")
logger.setLevel(logging.INFO)


MYSQL = 'mysql+pymysql://root:22380476@127.0.0.1/paper?charset=UTF8MB4'
POSTGRESQL = 'postgresql://postgres:22380476@127.0.0.1:7432/paper'

engine = create_engine(POSTGRESQL, pool_recycle=300, )
SessionMaker = sessionmaker(bind=engine)


# @event.listens_for(engine, "before_cursor_execute")
# def before_cursor_execute(conn, cursor, statement,
#                         parameters, context, executemany):
#     conn.info.setdefault('query_start_time', []).append(time.time())
#     # logger.debug("Start Query: %s", statement)
#
# @event.listens_for(engine, "after_cursor_execute")
# def after_cursor_execute(conn, cursor, statement,
#                         parameters, context, executemany):
#     total = time.time() - conn.info['query_start_time'].pop(-1)
#     # logger.debug("Query Complete!")
#     logger.info("Total Time: %f", total)
