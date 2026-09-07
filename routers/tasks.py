from fastapi import APIRouter, HTTPException, status , Depends
from routers.auth import get_current_user
from models.task import TaskCreate,Task
from services import taskService

router = APIRouter()


@router.post("/tasks",response_model=Task)
def createTask(task: TaskCreate ,current_user = Depends(get_current_user)):
    return taskService.create_Task(task,current_user.id)


@router.get("/tasks")
def getTasks(current_user = Depends(get_current_user)):
    return taskService.get_tasks(current_user.id)


@router.get("/tasks/{id}",response_model=Task)
def getTask(id: int,current_user = Depends(get_current_user)):

    task = taskService.get_task_by_ID(id,current_user.id)

    if task:
        return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Invalid task ID"
    )


@router.delete("/tasks/{id}",response_model=Task)
def removeTask(id: int,current_user = Depends(get_current_user)):

    task = taskService.remove_Task(id,current_user.id)

    if task:
        return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="No task found with that ID."
    )


@router.put("/tasks/{id}",response_model=Task)
def updateTask(newTask: TaskCreate, id: int,current_user = Depends(get_current_user)):

    task = taskService.update_Task(newTask, id,current_user.id)

    if task:
        return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="No task found with that ID."
    )