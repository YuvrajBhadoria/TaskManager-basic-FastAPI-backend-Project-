from fastapi import APIRouter, HTTPException, status
from services import userService
from models.users import User,UserCreate
import jwt
router = APIRouter()

@router.post("/register")
def register(user:UserCreate):
    userService.register(user)
    
@router.post("/login")
def login(user:UserCreate):
    loggedIn:User = userService.login(user)
    if loggedIn is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User Not Found"
        )
 
    SECRET_KEY = "my-secret-key"

    payload = {
        "sub": loggedIn.id
    }

    token = jwt.encode(payload , SECRET_KEY , algorithm="HS256")

    return {"access_token": token}
    
