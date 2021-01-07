import requests
import json

def send_update(stats):
    url = 'http://localhost:5000/r'
    payload = stats
    headers = {'content-type': 'application/json'}
    response = requests.post(url,data=json.dumps(payload), headers=headers)
    parsedDict = json.loads(response.text)
    return parsedDict