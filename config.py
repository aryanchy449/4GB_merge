import os

class Config(object):
    API_HASH = os.environ.get("API_HASH", "cbabdb3f23de6326352ef3ac26338d9c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7609226318:AAEAnsDJFhqDDtnNYe_BYYuScYSrsqAy8UE")
    TELEGRAM_API = os.environ.get("TELEGRAM_API", "9301087")
    OWNER = os.environ.get("OWNER", "1525203313")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "ASSAULTER_SHIV")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "BoB_Files1")
    PASSWORD = os.environ.get("PASSWORD", "Shiv")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Shivji:BoBfiles@cluster0.t1mka5v.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOG_CHANNEL", "-1002205049781")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQD6zg0ArR6gYuRUV-qFWswsYVSqCmBPwg8zlVoTrigYNiwHxr3B6H15Px3REqKqA8i1laeGAk3SXmFImOS6coY4OhzAHzyOrGeAPgYDKwzsj-BzfXXb2CNM_mIBMDv8KGisfix4-6lUrhB5LXtEEgVkyQcf6KFtnsi7aWaR3nRtbbX1E_3ANJ3aaiyvhgqQtp3mkZsbwIVGCB4PUuJI-6hmWhs_BSfayydpYTGFV9qV8-8K3PgpYO2d8f0G3I97DP2Q_MG5UsXsokzsfhrThtcno-2mRGGwNtBKRrmqNi2ijaOZVxS8rqSvruFlD2m7tOr2Jj6BeWVsSVIw88bhLpOjyeI2vAAAAABa6MFxAA")
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
    UPSTREAM_REPO = "https://github.com/shiv9969/4GB_merge"
    UPSTREAM_BRANCH = "master"

    START_TEXT = """
Hɪ 👋 I Aᴍ A Fɪʟᴇ/Vɪᴅᴇᴏ Mᴇʀɢᴇ Bᴏᴛ. I Cᴀɴ Mᴇʀɢᴇ Tᴇʟᴇɢʀᴀᴍ Fɪʟᴇs!, Aɴᴅ Uᴘʟᴏᴀᴅ Iᴛ Tᴏ Tᴇʟᴇɢʀᴀᴍ.

"""
