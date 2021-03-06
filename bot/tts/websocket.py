import json
from enum import IntEnum

from aiohttp import WSMsgType
from discord import Client


class Close(Exception):
    pass


class ReceiveType(IntEnum):
    COMMAND = 0
    HELLO = 1
    RECONNECT = 2


class SendType(IntEnum):
    HELLO = 1
    VERIFY = 2


class ttsDiscordWebSocket:
    def __init__(self, socket, client: Client):
        self.socket = socket
        self.loop = client.loop
        self.client = client

    @property
    def open(self):
        return not self.socket.closed

    async def close(self):
        await self.socket.close()

    @classmethod
    async def from_client(cls, client: Client):
        socket = await client.tts_http.ws_connect()
        print(socket)
        ws = cls(socket, client)

        await client.wait_until_ready()
        await ws.poll_event()

        return ws

    async def received_message(self, msg):
        data = json.loads(msg)
        receive_type = ReceiveType(data["type"])

        if receive_type == ReceiveType.HELLO:
            await self.send({"type": SendType.HELLO, "id": self.client.user.id})
            return

        if receive_type == ReceiveType.RECONNECT:
            print("reconnect")
            await self.close()
            raise Close

    async def poll_event(self):
        msg = await self.socket.receive()

        if msg.type == WSMsgType.TEXT:
            await self.received_message(msg.data)
        if msg.type in (WSMsgType.CLOSE, WSMsgType.CLOSED, WSMsgType.CLOSING):
            raise Close

    async def send(self, data):
        json_data = json.dumps(data)
        await self.socket.send_str(json_data)
