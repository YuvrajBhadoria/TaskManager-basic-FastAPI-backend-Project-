from models.task import TaskCreate 
from data.connection_pool import pool

def get_tasks(user_id):
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM tasks WHERE user_id=%s",
                           (user_id,))
            rows = cursor.fetchall()

    return [  {
            "id": row[0],
            "title": row[1],
            "completed": row[2]
        }
        for row in rows]

def get_task_by_ID(task_ID: int,user_id):
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM tasks WHERE id =%s AND user_id=%s",
                (task_ID,user_id,))
            row = cursor.fetchone()
    if row is None:
        return None
    return {
        "id": row[0],
        "title": row[1],
        "completed": row[2]
    }

def create_task(task,user_id):
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO tasks(title,completed,user_id)
                VALUES (%s,%s,%s)
                RETURNING id,title,completed,user_id
                   """,
                (task.title,task.completed,user_id)
            )
            row = cursor.fetchone()
    return {
            "id": row[0],
            "title": row[1],
            "completed": row[2]
        }
    

def remove_task(id: int,user_id):
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
            """
            DELETE FROM tasks WHERE id=%s AND user_id = %s
            RETURNING id,title,completed,user_id
            """,
                        (id,user_id,))
            row = cursor.fetchone()
    if row is None:
            return None
    return {
                "id": row[0],
                "title": row[1],
                "completed": row[2]
            }

def update_task(newTask: TaskCreate,id:int,user_id):
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
            """
            UPDATE tasks SET title =%s,completed =%s WHERE id=%s AND user_id = %s
            RETURNING id,title,completed,user_id
            """,
                        (newTask.title,newTask.completed,id,user_id))
            row = cursor.fetchone()
    if row is None:
            return None
    return {
                "id": row[0],
                "title": row[1],
                "completed": row[2]
            }
