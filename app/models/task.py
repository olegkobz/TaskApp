import enum
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from datetime import datetime
class StatusEnum(str, enum.Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"

class PriorityEnum(enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, index=True, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(Enum(StatusEnum))
    priority = Column(Enum(PriorityEnum))
    project_id = Column(ForeignKey("projects.id"))
    assignee_id = Column(ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())
    due_date = Column(DateTime, default=datetime.utcnow())
    project = relationship("Project")
    assignee = relationship("User")