from fastapi import Header, HTTPException, status
from models.users import UserCreate,User
from services import userService

def get_current_user(username: str = Header(),password: str = Header()) -> User :
    
    credentials = UserCreate(
        username=username,
        password=password
    )

    user = userService.login(credentials)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid User"
        )
    
    currentUser = User(
        id=user["id"],
        username=user["username"]
    )
    
    return currentUser