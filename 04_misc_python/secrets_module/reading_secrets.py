import os
from pathlib import Path

from dotenv import load_dotenv

# https://youtu.be/8dlQ_nDE7dQ
# https://youtu.be/PYuTzLswn_Y

# parents[0] = 04_misc_python/, parents[1] = project root
_ENV_FILE: Path = Path(__file__).parents[1] / ".env"

load_dotenv(_ENV_FILE)  # injects .env variables into os.environ

print(os.getenv("SWAPI_BASE_URL"))
print(os.getenv("SECRET_1"))
print(os.getenv("SECRET_2"))
print(os.getenv("COMBINED"))
print(os.getenv("MAIL"))
print(os.getenv("DEMO_COMPANY"))
# all env variables load as str
print(os.getenv("DEMO_PORT"))
print(type(os.getenv("DEMO_PORT")))
