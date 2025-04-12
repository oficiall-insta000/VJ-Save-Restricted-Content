import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7907882693:AAG5xWJ8CpSiKbbc__T4MGhk5zDEwzXGf-c")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28889460"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a90d0079fb7d45a73ce8a35600942378")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5081207021"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
