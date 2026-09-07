import jwt
SECRET_KEY = "my-secret-key"

payload = {
    "sub": 2
}

token = jwt.encode(payload , SECRET_KEY , algorithm="HS256")

print(token)