import json
import os


def get_user_list(config, key):
    with open("{}/FallenRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True

    API_ID = "7440891"
    API_HASH = "18218ed0b82c5d35114982e85e6f8950"
    TOKEN = "5271178420:AAHeIbRCHJRtFelp5VJeb3A89mcvp1qpFvc"
    OWNER_ID = "5233742848"
    OWNER_USERNAME = "@an_unic_or_n47"
    SUPPORT_CHAT = "-1001576935752"
    JOIN_LOGGER = (-1001576935752)
    EVENT_LOGS = (-1001576935752)

    SQLALCHEMY_DATABASE_URI = "postgres://dllvhfnhluoqvs:2ffdfe571c122e4866c1519274c223c9c5a4c901f117f0634a7ca628f3fca0b9@ec2-3-227-146-146.compute-1.amazonaws.com:5432/d1gc4h0m9nc7l4"
    MONGO_DB_URI = "mongodb+srv://anu:anu@cluster0.jrsohmr.mongodb.net/?retryWrites=true&w=majority"
    LOAD = []
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    URL = None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    DONATION_LINK = ""
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = (
        "CAACAgUAAxkBAAEDafNhq5Z0DegqVzauwSighMw5cPWp8QACVgQAAuUG0FRXfCEuBziNzCIE"
    )
    ALLOW_EXCL = True
    CASH_API_KEY = "GUHZKUCUR2HQL1YG"
    TIME_API_KEY = "DD6YGKX1SRC8"
    BL_CHATS = []
    SPAMMERS = None
    ALLOW_CHATS = True
    START_IMG = "https://te.legra.ph/file/93d0b55f321f1f42e373e.png"
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    ARQ_API_KEY = "LJMETG-DPHBCX-DGHJCD-TMFIGB-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    ALLOW_EXCL = None
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
