from fastapi import APIRouter, HTTPException, status,Depends
from fastapi.security import OAuth2PasswordRequestForm
from services import userService
from models.users import User,UserCreate
from datetime import datetime, timedelta, timezone
import jwt
import os
from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

@router.post("/register")
def register(user:UserCreate):
    userService.register(user)
    
@router.post("/login")
def login(user: OAuth2PasswordRequestForm = Depends()):
    
    loggedIn = userService.login( UserCreate(
            username=user.username,
            password=user.password
        ))
    
    
    if loggedIn is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User Not Found"
        )
 
    SECRET_KEY = os.getenv("SECRET_KEY")


    payload = {
        "sub": str(loggedIn["id"]),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=5)
    }

    token = jwt.encode(payload , SECRET_KEY , algorithm="HS256")

    return {"access_token": token,
            "token_type": "bearer"}
    
