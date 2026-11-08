import os
from dotenv import load_dotenv

load_dotenv()

for key in os.getenv("VARIABLENAMES").split(","):
    print(f"{key}: {os.getenv(key)}")


   