from fastapi import FastAPI, WebSocketDisconnect
from fastapi.testclient import TestClient


app = FastAPI()
clients = {}


@app.get("/")
async def get_root():
    return { "Hello": "World" }


@app.websocket_route("/ws")
async def websocket(ws):
    await ws.accept()
    await ws.send_json( { "Hello": "World" })
    await ws.close(1000)
    
    # key = ws.headers.get("sec-websocket-key")
    # clients[key] = ws
    
    """
    try:
        while True:
            # data = await ws.recive_json()
            for client in clients.values():
                await client.send_json({"a": "hello"})
    except WebSocketDisconnect:
        del clients[key]
        await ws.close()
    """

def test_api():
    client = TestClient(app)
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == { "Hello": "World" }

def test_ws():
    client = TestClient(app)
    with client.websocket_connect("/ws") as ws:
        data = ws.receive_json()
        print(data)
        assert data == { "Hello": "World" }