import uvicorn


if __name__ == "__main__":
    uvicorn.run("apps.main:app", host="localhost", port=8000, reload=True)
