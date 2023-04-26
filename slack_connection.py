import requests
import time
import os
import json
from dotenv import load_dotenv
from flags import delete_json_file

from flags import delete_json_file
load_dotenv()

def slack():
    f = open('jsonFiles/main.json')
    data = json.load(f) 
    url = os.getenv("SLACK_WEBHOOK_URL")
    message = data
    result = requests.post(url, json=message)
    if (result.text == "ok"):
        print('Message was send')
    else:
        print(result.text)
    f.close()
    time.sleep(120)
    delete_json_file()

# slack()