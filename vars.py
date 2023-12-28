from os import environ
import re

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

SESSION = environ.get("SESSION", "forward bot")
API_ID = int(environ["API_ID", 10098309])
API_HASH = environ["API_HASH", "aaacac243dddc9f0433c89cab8efe323"]
BOT_TOKEN = environ["BOT_TOKEN", "5473067352:AAER3bMhPjiNZQmkkU9LJSIX5BiH7WuA2z8"]
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", -1001505526419))
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '2056407064').split()]
TARGET_DB = int(environ.get("TARGET_DB", 0))
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/InvizHer/Piro-forword")
