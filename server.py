import uvicorn


if __name__ == "__main__":
    uvicorn.run("app.run:app", host="localhost", port=8000, reload=False)
