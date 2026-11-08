import os
from dotenv import load_dotenv

load_dotenv()

nb = os.getenv("NUMBER")

if(int(nb)%2==0):
    print("nice")
    exit(0)
else:
    print("not nice")
    exit(-1)

   
