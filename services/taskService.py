from models.task import Task, TaskCreate
from data import task

def get_tasks(userID):
    return task.get_tasks(userID)

def get_task_by_ID(task_id: int,userID):
    return task.get_task_by_ID(task_id,userID)


def create_Task(newTask: TaskCreate,userID):
    return task.create_task(newTask,userID)


def remove_Task(id: int,userID):
    return task.remove_task(id,userID)


def update_Task(newTask: TaskCreate, id: int,userID):
    return task.update_task(newTask,id,userID)