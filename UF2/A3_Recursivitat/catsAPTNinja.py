import requests
name = 'chartreux'
api_url = 'https://api.api-ninjas.com/v1/cats?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': 'die1+4/py0wSBbKsOLOMTw==csdOX2WuaRlCRH5U'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)