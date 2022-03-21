from fastapi import FastAPI
from apps.api import blog, account


app = FastAPI()

app.include_router(account.router)
app.include_router(blog.router)


@app.get("/")
async def root():
    return {"message": "Hello Daco!"}


@app.on_event("startup")
def on_app_start():
    print("서버가 시작되었습니다.")


@app.on_event("shutdown")
def on_app_shutdown():
    print("서버가 종료되었습니다.")
