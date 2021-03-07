from app import create_app

app = create_app()


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/ping")
async def ping():
    return "pong."
