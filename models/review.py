#!/usr/bin/python3
"""Review class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Represents a review for MySQL database.
    Inherits from SQLAlchemy Base and links to MySQL table reviews.
    Attributes:
        __tablename__ (str): Name of the MySQL table to store Reviews.
        text (sqlalchemy String): Review description.
        place_id (sqlalchemy String): Review's place id.
        user_id (sqlalchemy String): Review's user id.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
