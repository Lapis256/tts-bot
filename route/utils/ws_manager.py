import asyncio
import signal

from .ws_client import Client


class WSManager:
    def __init__(self):
        self.clients: list[Client] = []
        self.loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

        signal.signal(signal.SIGTERM, self.close)

    async def connect(self, client: Client):
        await client.accept()
        self.clients.append(client)

    def disconnect(self, client: Client):
        self.clients.remove(client)

    def close(self, signum, frame):
        for client in self.clients:
            self.loop.create_task(client.send({"type": 2}))
