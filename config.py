from dotenv import load_dotenv
import os

load_dotenv('.env')


class Config(object):

    TG_BOT_TOKEN = os.environ.get(
        "TG_BOT_TOKEN", "")
    APP_ID = int(os.environ.get("APP_ID", ))
    API_HASH = os.environ.get("API_HASH", "")

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    BANNED_USERS = set(int(x)
                       for x in os.environ.get("BANNED_USERS", "").split())
    MAX_FILE_SIZE = 1950000000
    TG_MAX_FILE_SIZE = 1950000000
    FREE_USER_MAX_FILE_SIZE = 1950000000
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    MAX_MESSAGE_LENGTH = 4096
    PROCESS_MAX_TIMEOUT = 1
    DEF_WATER_MARK_FILE = ""
