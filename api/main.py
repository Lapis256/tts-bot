from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

import interaction

app = FastAPI()
app.include_router(interaction.router)

clients = {}


@app.get("/")
async def get_root():
    return { "Hello": "World" }




# @app.websocket_route("/ws")
# async def websocket(ws):
#     await ws.accept()
#     await ws.send_json( { "Hello": "World" })
#     await ws.close(1000)
    
#     # key = ws.headers.get("sec-websocket-key")
#     # clients[key] = ws
    
#     """
#     try:
#         while True:
#             # data = await ws.recive_json()
#             for client in clients.values():
#                 await client.send_json({"a": "hello"})
#     except WebSocketDisconnect:
#         del clients[key]
#         await ws.close()
#     """
