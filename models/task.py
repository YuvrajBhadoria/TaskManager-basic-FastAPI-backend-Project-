from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    completed: bool

class Task(BaseModel):
    title: str
    completed: bool
    id: int