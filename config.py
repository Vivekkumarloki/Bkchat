from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "22475741"
# -------------------------------------------------------------
API_HASH = "1a217be71a0225e0a678af286c211f8a"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7250012103"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Vivekkumarloki/Bkchat")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
SUPPORT_GRP = "BRANDED_WORLD"
UPDATE_CHNL = "BRANDED_PAID_CC"
OWNER_USERNAME = "BRANDEDKING8"
# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", "")
    
