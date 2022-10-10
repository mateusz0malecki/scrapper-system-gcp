import os
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base


postgres_user = os.getenv("POSTGRES_USER")
postgres_db = os.getenv("POSTGRES_DB")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_host = os.getenv("POSTGRES_HOST")
postgres_port = os.getenv("POSTGRES_PORT")


Base = declarative_base()


def connect_tcp_socket() -> sqlalchemy.engine.base.Engine:
    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL.create(
            drivername="postgresql+pg8000",
            username=postgres_user,
            password=postgres_password,
            host=postgres_host,
            port=postgres_port,
            database=postgres_db,
        ),
    )
    return pool
