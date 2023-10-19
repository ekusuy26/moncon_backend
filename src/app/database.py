from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from typing_extensions import Annotated

from . import config
from functools import lru_cache


@lru_cache()
def get_settings():
    return config.Settings()


settings = get_settings()

SQLALCHEMY_DATABASE_URL = 'mysql://%s:%s@%s:%s/%s' % (
    settings.db_user,
    settings.db_pass,
    settings.db_host,
    settings.db_port,
    settings.db_name,
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
