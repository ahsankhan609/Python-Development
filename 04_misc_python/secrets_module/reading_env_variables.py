import os
from pathlib import Path

from dotenv import load_dotenv

# https://youtu.be/8dlQ_nDE7dQ
# https://youtu.be/PYuTzLswn_Y
# https://youtu.be/A1OA0Y9vwJY

# parents[0] = reading_env_variables/, parents[1] = 04_misc_python/, parents[2] = project root
_ENV_FILE: Path = Path(__file__).parents[2] / ".env"

load_dotenv(_ENV_FILE)  # injects .env variables into os.environ

print(os.getenv("SWAPI_BASE_URL"))
print(os.getenv("COMBINED"))
print(os.getenv("MAIL"))
print(os.getenv("DEMO_COMPANY"))
# all env variables load as str
print(os.getenv("DEMO_HOST"))
print(os.getenv("DEMO_PORT"))
