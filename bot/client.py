import asyncio
import aiohttp
from discord import Client
from discord.errors import ConnectionClosed, GatewayNotFound, HTTPException

from gateway import ttsDiscordWebSocket

class ttsClient(Client):
    async def tts_connect(self):
        while not self.is_closed():
            print(0)
            try:
                coro = ttsDiscordWebSocket.from_client(self)
                self.tts_ws = await asyncio.wait_for(coro, timeout=60.0)
                while True:
                    print("success")
                    await self.tts_ws.poll_event()

            except (OSError,
                    HTTPException,
                    GatewayNotFound,
                    ConnectionClosed,
                    aiohttp.ClientError,
                    asyncio.TimeoutError):
                pass

            await asyncio.sleep(30)

    async def connect(self, *, reconnect):
        self.loop.create_task(self.tts_connect())
        await super().connect(reconnect=reconnect)
