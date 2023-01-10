import requests

res = requests.get('http://google.com/').text
print(res)