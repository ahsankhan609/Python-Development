"""Reading environment variables from a .env file.

KEY POINTS:
* It is a way to store sensitive information in a file.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# https://youtu.be/8dlQ_nDE7dQ
# https://youtu.be/PYuTzLswn_Y
# https://youtu.be/A1OA0Y9vwJY
# https://youtu.be/riptPbTMLVQ

# parents[0] = reading_env_variables/, parents[1] = 04_misc_python/, parents[2] = project root
_ENV_FILE: Path = Path(__file__).parents[2] / ".env"

load_dotenv(_ENV_FILE)  # injects .env variables into os.environ

# load_dotenv(dotenv_path="custom_env_file.env")
# if we have custom name of our env file, then load it here to use it,
# instead of the default .env file.
# but why we use custom environment variables file?
# because we can have multiple env files for different environments,
# like development(.env.development), production(.env.production), testing(.env.testing), etc.
# and we can load the appropriate env file for the environment we are in.

print(os.getenv("SWAPI_BASE_URL"))
print(os.getenv("COMBINED"))
print(os.getenv("MAIL"))
print(os.getenv("DEMO_COMPANY"))
# all env variables load as str
print(os.getenv("DEMO_HOST"))
print(os.getenv("DEMO_PORT"))
