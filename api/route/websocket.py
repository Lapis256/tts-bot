# from fastapi import APIRouter


# clients = {}
# router = APIRouter(prefix="/ws")


# @router.websocket_route("")
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