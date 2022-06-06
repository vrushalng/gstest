import json
import traceback
from datetime import datetime

import requests


def posttowa():

    post_url = 'https://api.gupshup.io/sm/api/v1/msg'
    headers = {
        'apikey': "e5tywzfodnk005nfa58yaq4vvlq3eda5",
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        "channel": "whatsapp",
        'source': "917834811114",
        'destination': "918291207985",
        "src.name": "GFAccessAPITest",
        "message": {
            "type": "text",
            "text": "Hi, how are you?"
        }
    }
    resp = requests.post(post_url, headers=headers, data=data)
    print(resp.json())

    return resp


posttowa()
