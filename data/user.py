from models.users import UserCreate,User
from data.connection_pool import pool
from pwdlib import PasswordHash

def register(user:UserCreate):
    password_hash = PasswordHash.recommended()
    hashed_password = password_hash.hash(user.password)

    
    with pool.connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO users(username,hashed_password)
                    VALUES (%s,%s)
                       """,
                    (user.username,hashed_password)
                )

def login(user: UserCreate):
    password_hash = PasswordHash.recommended()

    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT * FROM users WHERE username = %s
                """,
                (user.username,)
            )
            row = cursor.fetchone()

    if row is None:
        return None

    if password_hash.verify(user.password, row[2]):
        return {
            "id": row[0],
            "username": row[1]
        }

    return None

def get_user_by_id(userId: int):
    with pool.connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT * FROM users WHERE id = %s
                    """,
                    (userId,)
                )
                row = cursor.fetchone()
    
    if row is None:
        return None
    
    return User(
        id=row[0],
        username=row[1]
    )