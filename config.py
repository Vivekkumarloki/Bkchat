from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "6435225"
# -------------------------------------------------------------
API_HASH = "4e984ea35f854762dcde906dce426c2d"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "5551813927"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AFK-HOTTY/nainxchatbot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
SUPPORT_GRP = "Nainsupport"
UPDATE_CHNL = "Nainbots"
OWNER_USERNAME = "faizog"
# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", "")
    
