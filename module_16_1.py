from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def boss_page():
    return "Главная страница"

@app.get("/user/admin")
async def admin_input():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def read_id(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user")
async def read_user(username: str, userage: int):
    return f"Информация о пользователе. 'Имя': {username}, 'Возраст': {userage}"

