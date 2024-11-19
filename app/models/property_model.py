from sqlalchemy import Column, Integer, String, Boolean, Float
from app.config.config import Base


class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)
    rent = Column(Float, nullable=False)
    is_available = Column(Boolean, default=True)
