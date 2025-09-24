from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import FastAPI, Depends, HTTPException, Request, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()

KEY_SECRET = "secret_key"
ALGORITHM = "HS256" # Алгоритм шифрования для JWT.
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # Создаем схему OAuth2 для получения токена.

# База данных пользователей
users_db = {
    "user1": dict(username="user1", password="password1", spending=5000.0),
    "user2": dict(username="user2", password="password2", spending=15000.0),
}

# Уровни бонусов с минимальными тратами и кэшбэком.
bonus_levels = [
    dict(level="Silver", min_spending=0, cashback=0.01),
    dict(level="Gold", min_spending=10000, cashback=0.02),
    dict(level="Platinum", min_spending=20000, cashback=0.03),
]

# Модель пользователя для валидации данных.
class User(BaseModel):
    username: str # Имя пользователя.
    password: str # Пароль пользователя.
    spending: float # Расходы пользователя.

# Фабрика для создания токенов.
class TokenFactory:
    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta = None):
        # Функция для создания токена. Устанавливает время истечения токена.
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        return jwt.encode({**data, "exp": expire}, KEY_SECRET, algorithm=ALGORITHM) # Возвращает закодированный токен.


@app.post("/token", response_model=dict) # Эндпоинт для получения токена.
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Получение пользователя из базы данных по имени пользователя.
    user = users_db.get(form_data.username)
    # Проверка правильности введенных учетных данных.
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=401, detail="Incorrect credentials", headers={"WWW-Authenticate": "Bearer"})
    # Создание токена с помощью фабрики токенов.
    access_token = TokenFactory.create_access_token({"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"} # Возвращает токен и его тип.


async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Функция для получения текущего пользователя на основе токена.
    try:
        payload = jwt.decode(token, KEY_SECRET, algorithms=[ALGORITHM]) # Декодирование токена.
        username = payload.get("sub") # Получение имени пользователя из токена.
        if not username or not (user := users_db.get(username)):
            raise HTTPException(status_code=401, detail="Invalid credentials", headers={"WWW-Authenticate": "Bearer"})
        return User(**user)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials", headers={"WWW-Authenticate": "Bearer"})


@app.get("/bonus", response_model=dict) # Эндпоинт для получения информации о бонусах.
async def read_bonus_data(current_user: User = Depends(get_current_user)):
    spending = current_user.spending # Получение расходы текущего пользователя.
    sorted_levels = sorted(bonus_levels, key=lambda x: x["min_spending"])
    current_level = next((l for l in reversed(sorted_levels) if spending >= l["min_spending"]), None)
    next_level = next((l for l in sorted_levels if spending < l["min_spending"]), "No higher level")
    return {"current_level": current_level, "next_level": next_level}


# Middleware для проверки токена
@app.middleware("http")
async def check_token_middleware(request: Request, call_next):
    if request.url.path.startswith("/bonus"):  # Проверяет только защищенные маршруты
        token = request.headers.get("Authorization")
        if token is None or not token.startswith("Bearer "):
            return Response("Authorization token missing", status_code=401)
        token = token.split(" ")[1]
        try:
            payload = jwt.decode(token, KEY_SECRET, algorithms=[ALGORITHM])
            username = payload.get("sub")
            if not username or username not in users_db:
                return Response("Invalid token", status_code=401)
        except JWTError:
            return Response("Invalid token", status_code=401)

    response = await call_next(request)
    return response
