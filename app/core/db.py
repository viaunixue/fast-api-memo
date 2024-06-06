from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from app.core.config import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

