from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    owner = relationship("User", back_populates="projects")
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())
    is_archived = Column(Boolean, default=False)
