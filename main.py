from fastapi import FastAPI
from app.routers import user, project

app = FastAPI(
    title="Task Manager API",
    description="Backend for task management system",
    version="1.0.0"
)

app.include_router(user.router)
app.include_router(project.router)