import os
from dotenv import load_dotenv

load_dotenv()   # loads the .env file

api_key = os.getenv("key")

print(api_key)
hahahahgit 