from discord import client
import os
import dotenv

from client import ttsClient


client = ttsClient()

dotenv.load_dotenv()
client.run(os.environ["TOKEN"])
