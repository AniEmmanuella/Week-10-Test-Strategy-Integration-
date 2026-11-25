import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.database import initialize_database
from app.service import create_task, get_task, complete_task, TaskNotFoundError

DB_PATH = os.getenv("TASK_DB_PATH", "tasks.db")
initialize_database(DB_PATH)

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)

app = FastAPI(title="Task Service", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/tasks", status_code=201)
def add_task(payload: TaskCreate):
    try:
        return create_task(DB_PATH, payload.title)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))

@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    try:
        return get_task(DB_PATH, task_id)
    except TaskNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc))

@app.patch("/tasks/{task_id}/complete")
def mark_task_complete(task_id: int):
    try:
        return complete_task(DB_PATH, task_id)
    except TaskNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
