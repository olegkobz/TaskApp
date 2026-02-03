from sqlalchemy.orm import Session
from app import models, schemas

def get_project(db:Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()

def get_project_by_name(db:Session, name:str):
    return db.query(models.Project).filter(models.Project.name == name).first()

def create_project(db:Session, project:schemas.ProjectCreate):
    db_project = models.Project(
        name = project.name,
        description = project.description,
        owner_id = project.owner_id
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project