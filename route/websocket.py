from fastapi import APIRouter, WebSocketDisconnect, WebSocket  # noqa

from .utils.ws_client import Client
from .utils.ws_manager import WSManager

manager = WSManager()
router = APIRouter()


@router.websocket("/ws")
async def websocket(ws: WebSocket):
    client = Client(ws)
    await manager.connect(client)
    await client.send({"type": 1})
    data = await client.receive()

    if data["type"] == 1:
        client.set_id(data["id"])

    try:
        while True:
            await client.receive()

    except WebSocketDisconnect:
        manager.disconnect(client)
