from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from app import schemas, crud, models
from app.database import get_db

router = APIRouter(prefix="/projects", tags=["projects"])
@router.post("/", response_model=schemas.ProjectRead)
def create_project_endpoint(project:schemas.ProjectCreate, db:Session = Depends(get_db)):
    existing_project = db.query(models.Project).filter(models.Project.name == project.name).first()
    if existing_project:
        raise HTTPException(status_code=400, detail="Project already created")
    return crud.create_project(db, project)