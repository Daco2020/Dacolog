from fastapi import FastAPI
from apps.api import blog, account


app = FastAPI()

app.include_router(account.router)
app.include_router(blog.router)


@app.get("/")
async def root():
    return {"message": "Hello Daco!"}