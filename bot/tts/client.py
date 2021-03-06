import asyncio
from discord import Client

from aiohttp import ClientConnectionError

from tts.websocket import ttsDiscordWebSocket, Close
from tts.http import TTSHTTPClient


class ttsClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tts_http = TTSHTTPClient(loop=self.loop)
        self.tts_ws = None

    async def tts_connect(self):
        while not self.is_closed():
            print(0)
            try:
                coro = ttsDiscordWebSocket.from_client(self)
                self.tts_ws = await asyncio.wait_for(coro, timeout=60.0)
                while True:
                    await self.tts_ws.poll_event()

            except (asyncio.TimeoutError, ClientConnectionError, Close):
                pass

            await asyncio.sleep(30)

    async def connect(self, *, reconnect):
        self.loop.create_task(self.tts_connect())
        await super().connect(reconnect=reconnect)

    async def close(self):
        await self.tts_http.close()

        if self.tts_ws is not None and self.tts_ws.open:
            await self.tts_ws.socket.close()

        return await super().close()
