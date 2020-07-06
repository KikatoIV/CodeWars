import requests
import json

url = 'https://www.hackthebox.eu/api/invite/generate'
headers = {'Content-type': 'application/json; charset=utf-8', 'Accept': 'text/json', 'user-agent' : 'anything!'}
payload = {'key': 'value'}

r = requests.post(url, data=json.dumps(payload), headers=headers)

print(r.status_code)