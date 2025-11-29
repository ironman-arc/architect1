from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Iron Man HUD is alive"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Iron Man HUD is alive"}



