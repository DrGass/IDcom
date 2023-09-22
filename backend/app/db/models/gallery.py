from ..session import Base
from fastapi import HTTPException, status
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import Session

class Gallery(Base):
    __tablename__ = ''
    