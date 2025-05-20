from fastapi import FastAPI
from services.utils.crawler import crawler

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}
