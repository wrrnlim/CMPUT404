import requests

res = requests.get('https://raw.githubusercontent.com/wrrnlim/CMPUT404/main/lab1/getRequest.py').text
print(res)