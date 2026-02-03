from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProjectBase(BaseModel):
    name: str

class ProjectCreate(ProjectBase):
    description: Optional[str]
    owner_id: int

class ProjectRead(ProjectBase):
    id: int
    description: Optional[str]
    created_at: datetime
    owner_id: int
    class Config:
        from_attributes = True