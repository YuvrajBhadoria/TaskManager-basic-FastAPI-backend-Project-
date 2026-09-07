from models.users import User
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from services import userService
import jwt
import os
from dotenv import load_dotenv
load_dotenv()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = os.getenv("SECRET_KEY")

def get_current_user(
    token: str = Depends(oauth2_scheme)
) -> User:
    try:
        payload: dict = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        userID = int(payload.get("sub"))
       
        user = userService.get_user_by_id(userID)
        if user is None:
            raise HTTPException(
                            status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="User Not Found"
                        )
        return user
    except jwt.InvalidTokenError:
         raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials"
            )