from fastapi import FastAPI
import uvicorn

from .routers import play_router

app = FastAPI()

app.include_router(play_router.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
