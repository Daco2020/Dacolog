import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "blog.app:app", host="localhost", port=8000, reload=False
    ) 