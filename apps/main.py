from fastapi import FastAPI, Request
from apps.model import connector


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/{user_id}/logs")
async def logs(request: Request, user_id: int):
    print(request)
    return {"message": f"{user_id}번 유저의 블로그를 준비중입니다."}


@app.post("/users")
async def users(request: Request):
    print(f"{request['user']}")
    pass


@app.on_event("startup")
def on_app_start():
    print("서버가 시작되었습니다.")
    connector.connect()


@app.on_event("shutdown")
def on_app_shutdown():
    print("서버가 종료되었습니다.")
