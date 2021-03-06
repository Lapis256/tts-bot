import asyncio


from tts.client import ttsClient
from config import TOKEN

try:
    import uvloop
except ImportError:
    pass
else:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


client = ttsClient()


@client.event
async def on_ready():
    print("ready")


client.run(TOKEN)
