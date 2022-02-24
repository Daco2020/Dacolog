from fastapi import FastAPI, Request
from app.model import connector


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.on_event("startup")
def on_app_start():
    print("서버가 시작되었습니다.")
    connector.connect()


@app.on_event("shutdown")
def on_app_shutdown():
    print("서버가 종료되었습니다.")
