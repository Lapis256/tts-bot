from fastapi import WebSocket


class Client:
    def __init__(self, ws: WebSocket):
        self.ws = ws
        self.bot_id = None

    def set_id(self, id):
        self.bot_id = id

    async def accept(self):
        await self.ws.accept()

    async def send(self, data):
        await self.ws.send_json(data)

    async def receive(self):
        return await self.ws.receive_json()

    async def close(self):
        await self.ws.close()
