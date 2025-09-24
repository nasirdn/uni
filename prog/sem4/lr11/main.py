from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, Annotated

app = FastAPI()

class STaskAdd(BaseModel):
  name: str
  description: Optional[str] = None

class STask(STaskAdd):
  id: int

@app.post("/")
async def add_task(task: Annotated[STaskAdd, Depends()]):
  return {"data": task}

@app.get("/home")
def get_home():
  return {"text": "hello world!"}