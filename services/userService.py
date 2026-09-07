from models.users import UserCreate
from data import user
def register(newUser: UserCreate):
    user.register(newUser)

def login(existingUser: UserCreate):
    loggedIn = user.login(existingUser)
    if loggedIn is None:
        return None
    return loggedIn
