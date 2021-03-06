from urllib.parse import quote
import asyncio

import aiohttp
from discord.http import json_or_text

from config import WS_URL, API_URL


class Route:
    BASE = API_URL

    def __init__(self, method, path, **params):
        self.method = method
        self.path = path
        url = self.BASE + path
        if params:
            self.url = url.format(**{k: quote(str(v))
                                     for k, v in params.items()})
        else:
            self.url = url


class TTSHTTPClient:
    def __init__(self, loop=None):
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.__session = aiohttp.ClientSession(loop=self.loop)

    async def ws_connect(self):
        return await self.__session.ws_connect(WS_URL)

    async def close(self):
        if self.__session:
            await self.__session.close()

    async def request(self, route):
        method = route.method
        url = route.url

        async with self.__session.request(method, url) as r:
            data = await json_or_text(r)

            if r.status == 200:
                return data
