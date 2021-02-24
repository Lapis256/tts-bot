class ttsDiscordWebSocket:
    def __init__(self, socket):
        self.socket = socket

    @classmethod
    async def from_client(cls, client):
        session = client.http._HTTPClient__session
        socket = await session.ws_connect("wss://localhost:3000/ws", timeout=30.0)
        
        ws = cls(socket)
        return ws
    
    async def poll_event(self):
        msg = await self.socket.receive(timeout=60.0)
        return msg
