import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = "6289589949:AAFz53nui7kVW-MczA0_2bZNY50aW88UggU"
INST_LOGIN = "animeinfinity06"
INST_PASS = "Yami@276"
db_auth = "postgresql://levi:levi@localhost/levibot"
admin_id = 2033411815
custom_api_url = str(os.getenv("custom_api_url"))
MEASUREMENT_ID = str(os.getenv("MEASUREMENT_ID"))
API_SECRET = str(os.getenv("API_SECRET"))
OUTPUT_DIR = "downloads"

BOT_COMMANDS = [
    {'command': 'start', 'description': '🚀Початок роботи / Get started🔥'},
    {'command': 'settings', 'description': '⚙️Налаштування / Settings🛠'},
    {'command': 'stats', 'description': '📊Статистика / Statistics📈'},
]

ADMINS_UID = [admin_id]
