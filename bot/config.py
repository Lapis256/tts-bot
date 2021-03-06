from os import environ

import dotenv

dotenv.load_dotenv()

TOKEN = environ["TOKEN"]
WS_URL = environ["WS_URL"]
API_URL = environ["API_URL"]
