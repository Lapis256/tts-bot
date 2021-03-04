from fastapi import FastAPI

from route.interaction import router as interaction_router

app = FastAPI(
    openapi_url=None,
    docs_url=None,
    redoc_url=None
)
app.include_router(interaction_router)


@app.get("/")
async def get_root():
    return {"Hello": "World"}


@app.get("/ping")
async def ping():
    return "pong."
