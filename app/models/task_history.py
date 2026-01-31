from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from datetime import datetime

class TaskHistory(Base):
    __tablename__ = "task_history"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    changed_by_id = Column(Integer, ForeignKey("users.id"))
    field_name = Column(String, nullable=False)
    old_value = Column(String)
    new_value = Column(String)
    changed_at = Column(DateTime, default=datetime.utcnow())
    task = relationship("Task")
    changed_by = relationship("User")