from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

users = {'1':'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: str, age: str):
    keys_users = list(users.keys())
    if len(keys_users) == 0:
        new_id = 1
    else:
        for i in range(len(keys_users)):
            keys_users[i] = int(keys_users[i])
        new_id = max(keys_users) + 1
    description = 'Имя: ' + username + ', возраст: ' + age
    users.update({str(new_id): description})
    return f'User {str(new_id)} is registered'

@app.put("/user/{user_id}/{username}/{age}'")
async def update_user(user_id: str, username: str, age: str):
    for user in users:
        if user == user_id:
            users[user_id] = 'Имя: ' + username + ', возраст: ' + age
            return f"The user {user_id} is updated"
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    for user in users:
        if user == user_id:
            del users[user_id]
            return f"User {user_id} has been deleted"
    raise HTTPException(status_code=404, detail="User not found")
