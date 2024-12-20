from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/user/{user_id}")
async def read_id(user_id: Annotated[int, Path(ge=0, le=100, description='Enter User ID', example='2')]):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user/{username}/{age}")
async def read_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='Student')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='34')]):
    return f"Информация о пользователе. 'Имя': {username}, 'Возраст': {age}"

