from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}